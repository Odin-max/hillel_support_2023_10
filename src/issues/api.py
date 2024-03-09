# mypy: ignore-errors
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .models import Issue, Message
from .permissions import (
    IssueParticipant,
    RoleIsAdmin,
    RoleIsJunior,
    RoleIsSenior,
)
from .serializers import (
    IssueCreateSerializer,
    IssueReadonlySerializer,
    MessageSerializer,
)



class MessageList(APIView):

    permission_classes = [IsAuthenticated & ( IssueParticipant | RoleIsJunior
        | RoleIsSenior | RoleIsAdmin)]
    def get(self, request, issue_id):
        if not IssueParticipant().has_object_permission(request, self, issue_id):
            return Response(
                {"error":"You do not have permission to access this issue(s)"},
                status.HTTP_403_FORBIDDEN)

        messages = Message.objects.filter(issue_id=issue_id)
        serializer = MessageSerializer(messages, many = True)
        return Response(serializer.data)

    def post(self, request, issue_id):
        if not IssueParticipant().has_object_permission(request, self, issue_id):
            return Response(
                {"error":"You do not have permission to post this issue(s)"},
                status.HTTP_403_FORBIDDEN)
        
        request.data["issue"] = issue_id
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssueApiSet(ModelViewSet):
    queryset = Issue.objects.all()
    # permission_classes = [RoleIsAdmin]

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsSenior | RoleIsJunior | RoleIsAdmin]
        elif self.action == "create":
            permission_classes = [RoleIsJunior]
        elif self.action == "retrieve":
            permission_classes = [IssueParticipant]
        elif self.action == "update":
            permission_classes = [RoleIsSenior | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == "create":
            return IssueCreateSerializer
        return IssueReadonlySerializer


class MessageCreateAPI(CreateAPIView):
    serializer_class = MessageSerializer
    lookup_field = "issue_id"
    lookup_url_kwarg = "issue_id"
