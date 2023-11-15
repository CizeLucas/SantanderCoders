## Estruturas Concicionais e Loops
import random

"""
## saber se um aluno passou com sua media e se eh aplicado o conteito B
media = float(input("insira sua média: "))
conceito_b = True ##(True/False) Assume automaticamente que o aluno passaria caso fizesse a A.F. (nao faz A.F.)

if media > 10:
    print("Eita bixao, ta com media maior que 10??? Ta errado isso ai viu")
elif media >= 7:
    print("Vc foi aprovado por media, parabens!")
elif media>=4:
    if conceito_b:
        print("Vc passou por conceito B! Escapou por pouco :)")
    else:
        print("Voce vai precisar fazer a A.F.! :(")
else:
    print("Infelizmente Vc reprovou! :(")
"""

"""
##joguinho para acertar um numero aleatorio: 
numero_secreto  = random.randint(1,15) ## ambos extremos 1 e 15 inclusos
print("Tente acertar um numero gerado aleatoriamente entre 1 e 15:")
chute_usuario = -1;
qtd_de_chutes=1;
while(numero_secreto != chute_usuario):
    chute_usuario = int(input(f"chute {qtd_de_chutes}: "))
    qtd_de_chutes+=1
print("Parabens, vc acertou! (precisou de "+str(qtd_de_chutes)+")")
"""

"""
Parametros da funcao range():
range(x) -> vai de 0 ate (x-1)
range(x,y)-> vai de 1 ate (y-1)
range(x,y,z) -> vai de 1 ate (y-1) com incrementos de z (com z obrigatoriamente diferente de zero e inteiro)
"""
i=2 ## valor inicial para o loop for 
incremento = 2 ## incremento de cada iteracao
valor_de_parada = 10 ## valor (exclusivo) de parada 
for i in range(i, valor_de_parada, incremento): ## eh gerada uma nova variavel "i" em outro escopo
    print(i)