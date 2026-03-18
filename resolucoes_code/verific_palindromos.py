# 6 - Verificando Palíndromos 🔄
# Descrição: Vamos testar se uma palavra é um palíndromo?! 

# 1º Passo: Recebendo Dados

print("Bem-vindo ao incrível Testador de Palíndromos do Ítalo! 🎪🚀")
print("Palíndromo é uma palavra, frase ou um número que permanece exatamente igual quando lido de trás para frente!")
print("Exemplos: 'arara', 'Socorram-me, subi no onibus em Marrocos' (sim, até frases funcionam! 🤯)")
print("Lembre-se: não use acentos e digite apenas uma palavra.")
print("-" * 40) # Isso faz uma linhazinha de separação super estilosa! ➖

# Agora sim, pedimos o input com uma mensagem mais curta!
string = input("Dados para análise de Palíndromo, sem acentos: ")

# 2º Passo: Deixar tudo minúsculo 🔡
string_limpa = string.lower()

# 3º Passo: Tirar os espaços em branco 💨
string_limpa = string_limpa.replace(" ", "")

# 4º Passo: Tirar a pontuação (hífen e vírgula) ✂️
string_limpa = string_limpa.replace("-", "")
string_limpa = string_limpa.replace(",", "")

# Agora sim! A mágica da inversão! 🪄🔄
string_invertida = string_limpa[::-1]

print("A palavra original é:", string_limpa)
print("A palavra invertida é:", string_invertida)


# O grande teste! ⚖️🏆
if string_limpa == string_invertida:
    print(f"Uau! A palavra '{string_limpa}' é igual a '{string_invertida}'. É UM PALÍNDROMO! 🎉🥳🎈")
else:
    print(f"Poxa! '{string_limpa}' é diferente de '{string_invertida}'. NÃO é um palíndromo! 😅")
