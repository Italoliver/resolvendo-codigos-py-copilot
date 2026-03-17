# 4 - Verificando Números Pares e Ímpares 🧮
# Solicitando um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Verificando se o número é par ou ímpar usando o operador de módulo (%)
if numero % 2 == 0:
    print(f"O número {numero} é PAR! 🎈")
else:
    print(f"O número {numero} é ÍMPAR! 🌟")
