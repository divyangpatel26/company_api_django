from django.http import HttpResponse


def home_page(request):
    print("home page reqested")
    return HttpResponse("Url requested")
