from imc import calcular_imc, classificar_imc
from notas import media_notas, situacao_aluno
from temperatura import celsius_para_fahrenheit, celsius_para_kelvin

print("calculadora de imc")

peso = float(input("peso (kg): "))
altura = float(input("altura (m): "))

imc = calcular_imc(peso, altura)
print(f"seu imc e {imc:.2f}, classificacao: {classificar_imc(imc)}")

print("\nmedia de notas")
nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))

media = media_notas([nota1, nota2, nota3])
print(f"media: {media:.2f}, situacao: {situacao_aluno(media)}")

print("\nconversao de temperatura")
celsius = float(input("temperatura em celsius: "))
print(f"{celsius}C = {celsius_para_fahrenheit(celsius):.2f}F = {celsius_para_kelvin(celsius):.2f}K")
