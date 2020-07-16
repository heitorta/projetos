from time import sleep
print('Quantos m² de parede você quer pintar? ')
paredelarg=float(input('Qual a largura da parede? '))
sleep(0.5)
paredecomp=float(input('Qual o comprimento da parede? '))
sleep(0.5)
area=paredecomp * paredelarg
print(f'A área de: {paredelarg}*{paredecomp} é = {area}')
sleep(0.5)
print('Agora, quanta tinta você irá usar')
#A quantidade de tinta está medida em L/2m².
tinta=area*2
sleep(0.5)
print(f'A quantidade de tinta necessária será de {tinta}L para {area}m².')
print('Obrigado por usar o nosso programa. Volte sempre!')



