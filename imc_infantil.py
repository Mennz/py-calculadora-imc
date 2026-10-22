from imc import calcular_imc


# tabela de verdade usa percentil por idade em meses, aqui simplifiquei por faixa de anos
def classificar_imc_infantil(imc, idade):
    if idade <= 5:
        baixo, normal, alto = 14, 17, 18
    elif idade <= 10:
        baixo, normal, alto = 14.5, 18.5, 21
    else:
        baixo, normal, alto = 15.5, 21, 25

    if imc < baixo:
        return "abaixo do peso"
    elif imc < normal:
        return "peso normal"
    elif imc < alto:
        return "sobrepeso"
    else:
        return "obesidade"


def calcular_imc_infantil(peso, altura, idade):
    imc = calcular_imc(peso, altura)
    return imc, classificar_imc_infantil(imc, idade)
