from django.shortcuts import render

def codigo1(request):
    return render(request, 'codigo1.html')

def codigo2(request):
    return render(request, 'codigo2.html')
