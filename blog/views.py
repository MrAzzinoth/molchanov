from django.http import HttpResponse
from django.shortcuts import render

def posts_list(request):
    n = ['Oleg', 'Nigga', 'Ktoto', 'Nikto']
    return render(request, 'blog/index.html', context={'names': n})
