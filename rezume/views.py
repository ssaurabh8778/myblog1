from django.shortcuts import render

from django.shortcuts import render


def rezume(request):
    return render(request, 'rezume/index.html')