from django.shortcuts import render

def pagina_principal(request):
    return render(request, 'encontro/pagina_principal.html', {})
