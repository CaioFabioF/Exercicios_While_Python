import random

r = random.randint(0,10)
c = int(input('Adivinhe um valor de 0 até 10: '))
t = 1
while c != r :
    c = int(input('Adivinhe um valor de 0 até 10: '))
    t += 1
print('Acertou, você levou {} tentativas'.format(t))