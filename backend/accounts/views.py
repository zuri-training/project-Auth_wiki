from django.http import HttpResponse
# from django.shortcuts import render


def signup_view(request):
    # return render(request, 'aboutpage.html')
    return HttpResponse("Registration page")


def signin_view(request):
    # return render(request, 'homepage.html')
    return HttpResponse("Login page")


def logout_view(request):
    # return render(request, 'contactpage.html')
    return HttpResponse("Logout page")
