from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey ur at the index page now")