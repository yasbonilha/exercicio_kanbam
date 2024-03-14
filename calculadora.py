from adicao import adicao
from subtracao import subtracao
from multiplicacao import multiplicacao
from divisao import divisao

operacao = int(input("qual operação você deseja?\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão"))
a = int(input("digite o primeiro numero: "))
b = int(input("digite o segundo numero: "))
while operacao >0 & operacao < 5:
    switch_case = {
        1: adicao(a, b),
        2: subtracao(a, b),
        3: multiplicacao(a, b),
        4: divisao(a, b),
        "default" : "opção não encontrada"
    }


if operacao not in switch_case:
    switch_case["default"]
else:
    print(switch_case[operacao](a, b))