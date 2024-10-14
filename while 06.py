print('Programa para mostra PA')
a = int(input('Digite o primeiro termo da PA: '))
b = int(input('Digite a razão da PA: '))
c = 1
d = 0
e = 10
while e != 0 :
    d = d + e
    while c <= d :
        print(a+b)
        a += b
        c += 1
    print('Pausa')
    e = int(input('Digite quantos termos a mais quer ser apresentados: '))
    if e == 0 :
        print('Fim')
        print(d)
