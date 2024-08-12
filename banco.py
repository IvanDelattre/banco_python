menu = '''
Operações disponíveis:

-[d] depositar
-[s] sacar
-[e] extrato
-[q] sair

=>'''

def chamar_menu():
    print(menu,end=' ')
    operation = input("Digitar operação: ")
    

    return operation


extrato = ''
saldo = 0
numero_depositos = 0

numero_saques = 0
maximo_saques = 3
limite = 500
extrato_saque = ''

print(menu,end=' ')
operation = input("Digitar operação: ")

while True : 
    if operation != 'd' and operation != 's' and operation != 'e' and operation != 'q':
        print('<<***Operação Inválida***>>')
        operation = input("Digitar operação: ")
        continue
    
    match operation:
        case 'd':
            deposito = float( input("Valor do Depósito: R$ "))
            
            if deposito <= 0 :
                print('<< VALOR DEPÓSITO ÍNVALIDO >> ')
                print(menu,end=' ')
                operation = input("Digitar operação: ")
                continue

            numero_depositos += 1
            extrato += f'{numero_depositos}ª depósito : R${deposito}\n'
            saldo += deposito
            
        case 's':
            saque = float( input("Valor do sque : R$ "))
            if saque > limite :
                print('<< VALOR DE SAQUE ÍNVALIDO >> ')
                print(menu,end=' ')
                operation = input("Digitar operação: ")
                continue
        
            if maximo_saques == 0 :
                print('<<**LIMITE DO SAQUE ATINGIDO**>>')
                operation = chamar_menu()
                continue

            if saque > saldo : 
                print('\n<< ***VALOR NÃO DISPÓNIVEL NA CONTA CORRENTE** >> \n')
                operation = chamar_menu()
                continue

            numero_saques += 1
            extrato_saque += f'{numero_saques}ª saque : R$ {saque}\n'
            saldo -= saque
            maximo_saques -= 1

        case 'e':
            print("\nLista - Operaçõs de Depósito : \n")
            print(extrato)
            print('\nLista - Operações de saque : \n')
            print(extrato_saque)

        case 'q':
            print("\n<< Encerrado >>\n")
            break
        
            
    print("Saldo atual: ",saldo)


    print(menu,end=' ')
    operation = input("Digitar operação: ")


