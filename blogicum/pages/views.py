from django.shortcuts import render


# Create your views here.
def about(request):
    """Отображает страничку 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request):
    """Отображает страничку 'Правила'."""
    return render(request, 'pages/rules.html')
