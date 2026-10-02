from imc import calcular_imc

print("calculadora de imc")

peso = float(input("peso (kg): "))
altura = float(input("altura (m): "))

imc = calcular_imc(peso, altura)
print(f"seu imc e {imc:.2f}")
