from django.shortcuts import render

def index(request):
    return render(
        request,
        'public/pages/index.html',
    )
