d = 0
c = 1
e = []
f = 0
print('--'*50)
while c == 1:
    a = int(input('Digite 1 para somar valores e 2 para acabar a repetição: '))
    if a == 1 :
        b = int(input('Digite um valor: '))
        d += b
        f += 1
        e.append(b)
        print('O menor número é {} e o maior é {}'.format(min(e), max(e)))
        print('A média entre todos os valores foi: {}'.format(d/f))
        print('--'*50)
    if a == 2 :
        c += 1
if c == 2 :
    print('Fim')
    print('--'*50)