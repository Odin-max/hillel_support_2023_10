# mypy: ignore-errors
import json

from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from rest_framework import permissions, serializers, status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from .models import User
from .services import send_user_activation_email


# FBV
def create(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST requests")

    data: dict = json.loads(request.body)
    # role = data.get("role", "default_role")
    user: User = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")

    # convert to dict
    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}

    return JsonResponse(payload)


class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(
        choices=["junior", "senior"], required=False, default="junior"
    )

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "role"]
        # fields = "__all__"

    def validate(self, attrs: dict) -> dict:
        attrs["password"] = make_password(attrs["password"])

        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]


# CBF
class UserCreateAPI(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        send_user_activation_email(email=serializer.data["email"])
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserRetrieveAPI(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def get(self, request):
        return super().get(request)
