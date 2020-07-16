print('Olá! Resolva equações do tipo ax² + bx + c = 0')
import cmath
a=float(input('a = '))
b=float(input('b = '))
c=float(input('c = '))
Δ=(b**2) - (4*a*c)
print('Cálculo de Δ: b² - 4ac ')
print('O valor de Δ = ', Δ)

from time import sleep
sleep(1)
print('A equação montada:',a, 'x²','+', b, 'x','+',c)

sleep(1)
x1=(-b-cmath.sqrt(Δ))/(2*a)
x2=(-b+cmath.sqrt(Δ))/(2*a)
print('As soluções são: {} e {}'.format(x1,x2))

sleep(1)
print('Conjunto solução: X∈R/X=',x1,'ou', x2)





