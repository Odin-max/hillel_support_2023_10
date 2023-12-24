from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView

from .permissions import RoleIsAdmin, RoleIsJunior, RoleIsSenior, IssueParticipant
from .models import Issue
from .serializers import IssueCreateSerializer, IssueReadonlySerializer, MessageSerializer


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