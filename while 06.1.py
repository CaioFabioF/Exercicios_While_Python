a = int(input('Digite o primeiro termo da PA: '))
b = int(input('Digite a razão da PA: '))
# d é o contador
d = 1 
# t é o total de termos apresentados na PA
t = 0
# m é a quantidade inicial de termos apresentados na PA
m = 10
while m != 0 :
    t = t + m
    while d <= t :
        print(a+b)
        a += b
        d += 1
    print('Pausa')
    m = int(input('Quantos termos você quer mostrar a mais? '))
    if m == 0 : 
        print('O total de termos foi: {}'.format(t))
        print('Fim')
