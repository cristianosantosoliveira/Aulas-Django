from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


def index(request):
    html = f"<h1>Bem vindo `a { timezone.now()}</h1>"
    response = HttpResponse(html, status=404)
    response['ultimo_acesso'] = timezone.now()
    return response

def setacookie(request):
    response = HttpResponse()
    response.set_cookie("my_name", value="Cristiano")
    return response

def redireciona(request):
    return HttpResponseRedirect("https://www.uol.com.br")

def show_code(request, code):
     html = f"<h1>The code is: { code}</h1>"
     response = HttpResponse(html)
     return response

def cat_status(request, code):
     HttpResponseRedirect(f'https://http.cat/{code}')


def show_get_values(request):
    nome = request.GET.get("Nome: ", None)
    if nome is None:
        html = f"<h1>Bem vindo ao usuário anomino </h1>"
    else:
        html = f"<h1>Bem vindo ao usuário {nome}</h1>"
    return HttpResponse(html)

@csrf_exempt
def show_post_values(request):
    head = ""
    if request.method == "POST":
        nome =  request.POST.get("nome")
        sobrenome = request.POST.get("sobrenome")
        head += f"<h1> bem vindo {nome} {sobrenome} </h1>"
    html = """
    <form method=POST>
    <label for="nome">First name:</label><br>
    <input type="text" id="nome" name="nome" value=""><br>
    <label for="sobrenome">Sobrenome:</label><br>
    <input type="text" id="sobrenome" name="sobrenome" value=""><br><br>
    <input type="submit" value="Submit">
    </form>
"""
    htl_to_response = head + html
    return HttpResponse(htl_to_response)

