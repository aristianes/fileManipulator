import random
import string


def gerar_nome():
    letras = string.ascii_lowercase
    nome = ''.join(random.choice(letras) for _ in range(8))
    return nome.capitalize()

with open('nome.txt','w') as arquivo:
    for _ in range(1000):
        nome = gerar_nome()
        arquivo.write(nome + '\n')