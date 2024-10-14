a = int(input('Digite o primeiro termo da PA: '))
b = int(input('Digite a razão da PA: '))
d = 1

while d <= 10 :
    print(a+b)
    a += b
    d += 1
print('Fim')
