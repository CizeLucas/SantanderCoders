import math

def funcao_teste(qtd, msg="fulano"):
    if(qtd>0):
        qtd-=1
        funcao_teste(qtd, msg)
        print(f"{qtd}): Bem vindo {msg}")
    
funcao_teste(2)
funcao_teste(2, "Python")

def volume_esfera(raio, qtd_casas_dec=5):
    return round((4*math.pi*raio**3)/3,qtd_casas_dec)

print(volume_esfera(5))