from django.shortcuts import render

def landingPage(request):
    context ={

    }

    return render(request, 'templates/base/landing.html', context)
