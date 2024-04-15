# mypy: ignore-errors
from django.contrib import admin
from django.urls import include, path

# # controller
# def foo(request):
#     data = get_message()  # model
#     response = JsonResponse(data)  # JsonResponse is view
#     # controller
#     return response


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
    path("issues/", include("issues.urls")),
]
