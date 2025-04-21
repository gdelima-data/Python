import random

x = random.randint(1, 10)
tentativas = 5

print('Um número aleatório entre 1 e 10 será gerado. Tente acertar, são cinco tentativas\n')
input('')

resposta = int(input('Faça sua jogada:\n'))
tentativas -= 1

while resposta != x and tentativas > 0:
    print('Tentativas: ', tentativas)
    resposta = int(input('Tente novamente:\n'))
    tentativas -= 1

if tentativas == 0:
    print('Boa tentativa! O número era:', x)
else:    
    print('Correto!')
