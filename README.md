# Calculadora de IMC e médias

Programa de console em Python com três calculadoras simples: IMC com classificação
por faixa, média de três notas com situação do aluno, e conversão de temperatura de
Celsius para Fahrenheit e Kelvin. O cálculo de IMC agora também guarda um histórico,
mostra a faixa de peso ideal, um gráfico em texto, e tem uma versão separada para
IMC infantil.

## O que pratiquei

- Separar o código em módulos por assunto (`imc.py`, `notas.py`, `temperatura.py`)
- `input()` e conversão de tipos com `float()`
- `if`/`elif` para faixas de valores e para o menu
- `while True` com `break` para repetir o menu até o usuário sair
- Salvar e carregar histórico em JSON (`historico.py`)
- Calcular uma faixa de valores (peso ideal) em vez de um número só
- Classificação simplificada de IMC infantil por faixa de idade
- Montar um gráfico simples em texto, marcando uma posição numa escala

## Como rodar

```
python main.py
```

Escolha uma das opções do menu e siga as perguntas no terminal.
