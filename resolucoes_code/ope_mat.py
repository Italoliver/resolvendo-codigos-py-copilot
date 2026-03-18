# 3 - Operações Matemáticas Simples 📐
# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# Solicitando os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitando a operação
print("\nEscolha a operação:")
print(" + para Soma")
print(" - para Subtração")
print(" * para Multiplicação")
print(" / para Divisão")
operacao = input("Qual operação você deseja realizar? ")

# Estrutura de decisão para calcular
if operacao == "+":
    resultado = num1 + num2
    print(f"\n✅ O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"\n✅ O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"\n✅ O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    # Verificação para não dividir por zero! ⚠️
    if num2 != 0:
        resultado = num1 / num2
        print(f"\n✅ O resultado da divisão é: {resultado}")
    else:
        print("\n❌ Erro: Não é possível dividir por zero! 😱")
else:
    print("\n🚫 Operação inválida! Tente novamente usando +, -, * ou /.")
