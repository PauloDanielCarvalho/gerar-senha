import string

from random import  choice
valores=''
valores+=string.ascii_letters
valores+=string.digits
valores+=string.punctuation

def gerar_senha(valores, tamanho):
    senha=''
    for i in range(tamanho):
        senha+=choice(valores)
    print(senha)
gerar_senha(valores,8 )
print('senha gerada')