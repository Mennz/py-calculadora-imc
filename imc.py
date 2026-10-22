# IMC = peso dividido pela altura ao quadrado
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "peso normal"
    elif imc < 30:
        return "sobrepeso"
    elif imc < 35:
        return "obesidade grau 1"
    elif imc < 40:
        return "obesidade grau 2"
    else:
        return "obesidade grau 3"


# faixa de imc considerada normal e a mesma usada no classificar_imc
def faixa_peso_ideal(altura):
    minimo = 18.5 * altura ** 2
    maximo = 24.9 * altura ** 2
    return minimo, maximo


def grafico_imc(imc):
    tamanho = 40
    escala_maxima = 50
    posicao = int(imc / escala_maxima * tamanho)
    posicao = min(posicao, tamanho - 1)

    barra = list("-" * tamanho)
    barra[posicao] = "O"
    return f"0 |{''.join(barra)}| {escala_maxima}"
