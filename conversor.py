from time import sleep
print('\33[1:30:45m+\33[m'*28)
print('\33[1:30:45mCONVERSOR DE BASES NÚMERICAS\33[m')
print('\33[1:30:45m+\33[m'*28)
nome = str(input('\33[1:35mInforme seu nome:'))
print('Bem vindo(a), {}! Aqui converteremos qualquer número inteiro!'.format(nome))
print('VAMOS COMEÇAR...')
sleep(2)
n = int(input('Digite um número inteiro:'))
print('Agora escolha uma das bases abaixo para conversão:')
print('\33[1:36m1 - converter para BINÁRIO\n2 - converter para OCTAL\n3 - converter para HEXADECIMAL\33[m')
escolha = int(input('\33[1:35mInforme o número da opção escolhida:'))
print('CONVERTENDO...')
sleep(3)
bin = bin(n)[2:]
oc = oct(n)[2:]
hex = hex(n)[2:]
if escolha == 1:
    print('O número {} é igual a {} em BINÁRIO!'.format(n, bin))
elif escolha == 2:
    print('O número {} é igual a {} em OCTAL!'.format(n, oc))
elif escolha == 3:
    print('O número {} é igual a {} em HEXADECIMAL!'.format(n, hex))

