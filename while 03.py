
c = 0
while c != 5 :
    a = int(input('Digite um valor: '))
    b = int(input('Digite um valor: '))
    c = int(input('''
     [1] para somar
     [2] para subtrair
     [3] para multiplicar 
     [4] para dividir
     [5] para sair 
     '''))
    if c == 1 :
        print(a+b)
    elif c == 2 :
        print(a-b)
    elif c == 3 :
        print(a*b)
    elif c == 4 :
        print(a/b)

if c == 5  :
    print('Acabou')
print('Fim')