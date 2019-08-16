print ('Bem Vindo ao GROGER BANK cadastre as seguintes informaçoes')

nome = input ('Digite seu nome:  ')
idade = input ('Digite sua idade: ')
saldo = input ('Digite seu saldo: ')

# digitar numeros no sistema

x = int(input("Digite 1 para fazer um saque \nDigite 2 para deposito\nDigite 3 para fazer um emprestimo\nDigite 4 para visualizar informaçoes\nDigite qualquer outro caracter para sair \n  "))




def saque(saldo):
    valor_saque = float(input("digite o valor do saque"))
    if valor_saque > 1000 and saldo < valor-saque:
        print("nao foi possivel realizar o saque")
    else:
        saldo - valor_saque
        print("saque aprovado")
        print("saldo atual: {}".format(saldo))

def deposito(saldo):
    valor_deposito = float1(input('digite o valor do seu deposito'))
    if valor_deposito >5000:
        print('deposito negado')
    else:
        saldo + valor_deposito

def emprestimo(idade, saldo):
    if idade >21 and saldo >= 1000:
        valor_emprestimo = float(input('digite o valor do seu emprestimo'))

        if valor_emprestimo >= 2000 and valor_emprestimo < 15*saldo:
            saldo + valor_emprestimo
            print()

    else:
        print("emprestimo negado devido a idade")

def infos():
    print(nome, idade, saldo)


if x == '1':
   (saque)

elif x == '2':
    (deposito)

elif x == '3':
    (emprestimo)

elif x == '4':
    (infos)


