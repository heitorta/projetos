print('Olá! Resolvedor de equações by Heitor')
print('*valor de X deve ser definido como 1 ou 0.*')
a=float(input('a = '))
b=float(input('b = '))
x=int(input('x = '))
print('Equação formada: ')
print(a,'x','+', b,'= 0')
from time import sleep
sleep(2.5)
if x != 0 :
    resultado= (-b)/a
    print('A solução é:', resultado)
if x == 0:
    resultado2= (-b) + 0
    print('A solução é: ', resultado2)

