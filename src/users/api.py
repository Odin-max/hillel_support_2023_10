import json  # type: ignore

from django.http import JsonResponse  # type: ignore
from django.views.decorators.csrf import csrf_exempt  # type: ignore

from .models import Issues, User  # type: ignore


def all(request):
    users = User.objects.all()
    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    results: list[dict] = []
    for user in users:
        payload = {attr: getattr(user, attr) for attr in attrs}
        results.append(payload)

    return JsonResponse({"result": results})


def create(request):
    if request.method != "POST":
        raise NotImplementedError("Only POST request")

    data: dict = json.loads(request.body)
    user: User = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")
    # convert to dict
    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}
    return JsonResponse({payload})


@csrf_exempt
def create_issue(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST requests are allowed"})

    data = json.loads(request.body)
    issue = Issues.objects.create(**data)

    if not issue:
        return JsonResponse({"Error": "Failed to create issue"})
    issue_data = {
        "title": issue.title,
        "body": issue.body,
        "timestamp": issue.timestamp,
        "junior_id": issue.junior_id,
        "senior_id": issue.senior_id,
        "status": issue.status,
    }

    return JsonResponse({"issue": issue_data})


@csrf_exempt
def get_issues(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET requests are allowed"})

    issues = Issues.objects.all()

    issue_list = []

    for issue in issues:
        issue_data = {
            "title": issue.title,
            "body": issue.body,
            "timestamp": issue.timestamp,
            "junior_id": issue.junior_id,
            "senior_id": issue.senior_id,
            "status": issue.status,
        }
    issue_list.append(issue_data)
    return JsonResponse({"issues": issue_list})
