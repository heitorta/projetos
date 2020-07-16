from time import sleep
print('Calculadora de reajuste salarial ')
sb=float(input('Qual o seu salário antes do reajuste? '))
sleep(0.4)
sr=sb+(0.15*sb)
sleep(0.4)
print(f'O seu salário de R${sb:.2f} pós reajuste ficou em R${sr:.2f}.')
sleep(0.15)




