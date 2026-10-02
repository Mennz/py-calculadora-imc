from imc import calcular_imc, classificar_imc
from notas import media_notas, situacao_aluno
from temperatura import celsius_para_fahrenheit, celsius_para_kelvin

while True:
    print("\n1 - calcular imc")
    print("2 - media de notas")
    print("3 - conversao de temperatura")
    print("4 - sair")
    opcao = input("escolha: ")

    if opcao == "1":
        peso = float(input("peso (kg): "))
        altura = float(input("altura (m): "))
        imc = calcular_imc(peso, altura)
        print(f"seu imc e {imc:.2f}, classificacao: {classificar_imc(imc)}")

    elif opcao == "2":
        nota1 = float(input("nota 1: "))
        nota2 = float(input("nota 2: "))
        nota3 = float(input("nota 3: "))
        media = media_notas([nota1, nota2, nota3])
        print(f"media: {media:.2f}, situacao: {situacao_aluno(media)}")

    elif opcao == "3":
        celsius = float(input("temperatura em celsius: "))
        f = celsius_para_fahrenheit(celsius)
        k = celsius_para_kelvin(celsius)
        print(f"{celsius:.2f}C = {f:.2f}F = {k:.2f}K")

    elif opcao == "4":
        break

    else:
        print("opcao invalida")
