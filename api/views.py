from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({"name": "NL LABS", "title": "Founder and CEO"})
