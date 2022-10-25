from time import sleep

print("-="*14)
print("     Caixa Eletrônico      ")
print("-="*14)

saldo = 1500
senha = '1981'
senha_saque = ''
nome = 'Caio'
agencia = '001'

opcao = input('Digite uma opção:\n1 - Para Saque\n2 - Para Deposito\n3 - Sair\nopção: ')
if opcao == '1':
    valor_saque = int(input('Digite o valor que deseja sacar: '))

    while senha_saque != senha:
        senha_saque = input('digite sua senha: ')
        print(f'---Saldo disponível na conta {saldo}')

    nome = input('Digite seu nome: ')
    agencia = input('Digite sua agencia: ') 

    if nome == 'Caio' and agencia == '001':
        print(f'Valor do saque {valor_saque}')
        if valor_saque <= saldo:
            print('---Saldo suficiente!')
            resp = input('Deseja fazer o saque? [S/N] ')
            if resp == 's':
                senha_saque = input('Senha para saque: ')
                print('---Cartão retirado. Aguarde o comprovante.')
                print(f'Comprovante de saque. Valor: {valor_saque}')
            elif resp == 'n':
                print('---Operação cancelada!')  
        else:
            print('---Saldo insuficiente!')

elif opcao == '2':
    deposito = int(input('Digite o valor do deposito: '))
    deposito = saldo + deposito
    print('Deposito feito com sucesso.')
    print(f'Saldo atual {deposito}')

else:
    print("Processo encerrado! Obrigado, volte sempre.")
