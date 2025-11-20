"""Views для 'статичных страниц сайта.

Содержит страницы с информацией о проекте, правилах и т.д.
"""
from django.shortcuts import render


# Create your views here.
def about(request):
    """Отображает страничку 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отображает страничку 'Правила'."""
    return render(request, 'pages/rules.html')
