from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
  msg = """
  <!DOCTYPE html>
  <html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello World</title>
    </head>
    <body>
      <h1>Seja bem vindo a atividade</h1>
      <p>Seja bem vindo a página home da atividade de Desenvolvimento Web II</p>
    </body>
    </html>
    
  """
  return HttpResponse(msg)

def index(request):
  msg = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora</title>
</head>
<body>
    <h1>Calculadora - Realize cálculos simples</h1>
    <p>Digite dois números e selecione uma operação para realizar o cálculo.</p>
    <form action="/calcular/" method="post">
        <label for="numero1">Número 1:</label>
        <input type="number" name="numero1" step="any" required>

        <label for="numero2">Número 2:</label>
        <input type="number" name="numero2" step="any" required>

        <label for="operacao">Operação:</label>
        <select name="operacao" required>
            <option value="soma">Soma</option>
            <option value="subtracao">Subtração</option>
            <option value="multiplicacao">Multiplicação</option>
            <option value="divisao">Divisão</option>
        </select>

        <button type="submit">Calcular</button>
    </form>
</body>
</html>   
  """
  return HttpResponse(msg)

@csrf_exempt
def calcular(request):
  if request.method == 'POST':
    numero1 = float(request.POST.get('numero1', 0))
    numero2 = float(request.POST.get('numero2', 0))
    operacao = request.POST.get('operacao')

    if operacao == 'soma':
        resultado = numero1 + numero2
        explicacao = f"Soma de {numero1} e {numero2}"
    elif operacao == 'subtracao':
        resultado = numero1 - numero2
        explicacao = f"Subtração de {numero1} e {numero2}"
    elif operacao == 'multiplicacao':
        resultado = numero1 * numero2
        explicacao = f"Multiplicação de {numero1} e {numero2}"
    elif operacao == 'divisao':
        if numero2 == 0:
            msg = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Erro</title>
            </head>
            <body>
                <h1>Erro</h1>
                <p>Divisão por zero não é permitida. Tente novamente.</p>
                <a href="/index/">Voltar</a>
            </body>
            </html>
            """
            return HttpResponse(msg)
        resultado = numero1 / numero2
        explicacao = f"Divisão de {numero1} por {numero2}"
    else:
        return HttpResponse("Operação inválida.")


    msg = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resultado</title>
    </head>
    <body>
        <h1>Resultado do Cálculo</h1>
        <p>Você realizou a seguinte operação:</p>
        <p>{explicacao}</p>
        <p><strong>Resultado:</strong> {resultado}</p>
        <a href="/index/">Voltar</a>
    </body>
    </html>
    """
    return HttpResponse(msg)
  else:
    return HttpResponse("Método inválido.")

def autor(request):
    msg = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Autor</title>
    </head>
    <body>
        <h1>Sobre o Autor</h1>
        <p>Iego Assis da Silva</p>
        <p>Formado em Licenciatura em Matemática, pós-graduado em Metodologia do Ensino de Matemática, Gestão Escolar e Coordenação Pedagógica</p>
           <li>Técnico em Informática para Internet</li>
         <a href="/home/">início</a>
    </body>
    </html>
  """
    return HttpResponse(msg)