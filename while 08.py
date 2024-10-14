a = 0
b = 0
c = 0
d = 0
while c != 999 :
    if c != 999 :
        c = int(input('Digite um valor: '))
        a += 1
        b += c
    if c == 999 :
        b -= 999
        d += 1
print('Foram digitados {} valores corretos, e a soma entre eles é {}. E foi digitado {} valor errado.'.format(a-1,b,d))