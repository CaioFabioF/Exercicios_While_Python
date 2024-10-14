s = str(input('Digite M para masculino, ou F para Feminino: ')).strip().upper()[0]
while s != 'M' and s != 'F' :
    s = str(input('Digite M para masculino, ou F para Feminino: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))