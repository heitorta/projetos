from time import sleep
print('SALDÃO RICARDO ELETRO')
preco=float(input('Valor do produto em R$: '))
desconto=preco - (0.05 * preco)
sleep(0.5)
print(f'O produto de valor R${preco:.2f} sai por R${desconto:.2f} no saldão de 5% da RICARDOELETRO!')


