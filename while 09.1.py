a = 0
b = 0
c = 0
d = 0
while a != 999:
    a = int(input('Digite um valor: '))
    if a != 999 :
        b += 1
        c += a
    
    if a == 999 :
        d += 1

print('A soma de todos os valores foi: {}'.format(c))
print('A quantidade de termos digitados foi: {}. E a foi digitado {} termo PROIBIDO!'.format(b,d))