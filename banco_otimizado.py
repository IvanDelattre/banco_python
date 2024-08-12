menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q]\tSair
    => """


def main():
    print(menu,end=' ')
    operation = input()
    extrato = ''
    saldo = 0
    limite_saques = 3
    usuarios  = []
    contas = []
    while True:
        
        if operation == 'd':

            deposito = float(input('Digite Valor de Depósito: R$ ') )
            extrato, saldo  = depositar(deposito, saldo , extrato )


        elif operation == 's':

            extrato , saldo , limite_saques = sacar(extrato , saldo , limite_saques )

        
        elif operation == 'e':
            imprimir_extrato(extrato, saldo )

        
        elif operation == 'nc':
            contas = criar_conta(usuarios,contas)

        
        elif operation == 'lc':
            listar_contas(contas)

        elif operation == 'nu':
            new_user(usuarios)


        elif operation == 'q' :
            print('\n<< ENCERRADO >>\n')
            break
        else:
            print('<<***Operação Inválida***>>')
            

        print(menu,end=' ')
        operation = input()


def depositar(deposito, saldo , extrato):
    print("\n================  ================")

    saldo += deposito
    extrato += f'Valor depósito: R$ {deposito:.2f} \n'

    print('Valor depósitavo com sucesso ')
    print("==========================================")

    return extrato , saldo 


def imprimir_extrato(extrato, saldo ):
    print("\n================ EXTRATO ================")
    print(extrato)
    print(f'Valor do saldo : R$ {saldo:.2f}')
    print("==========================================")



def sacar( extrato ,saldo  , limite):
    print("\n================  ================")

    if limite == 0 :
        print('\n<< Limite de saque diário atingido >>\n ')
        return extrato , saldo , limite
    
    saque = float( input('Digite Valor saque: R$ '))

    if saque > 500 :
        print('\nNão são permitidos valores maiores que R$500,00\n')
        return extrato , saldo , limite
    if saque > saldo :
        print('\nValor acima do saldo da conta\n ')
        return extrato , saldo , limite

    saldo -= saque
    limite -= 1
    extrato += f'Valor saque: R$ {saque:.2f} \n'
    print('Valor sacado  com sucesso ')
    print("==========================================")

    return extrato , saldo , limite


def percorrer_usuarios(usuarios, pessoa ) :
    for elemento in usuarios:
        if elemento['cpf'] == pessoa['cpf'] :
            return True
        
    return False


def encontar_usuarios(usuarios, pessoa ) :
    for elemento in usuarios:
        if elemento['cpf'] == pessoa['cpf'] :
            pessoa['pessoa'] = elemento 
            return True

      
    return False



def new_user(usuarios):
    print("================ CADASTRAR USUÁRIO ================\n")

    pessoa = dict()
    pessoa['nome'] = input('Digitar nome completo: ')
    pessoa['data'] = input('Digite data de nascimento dd-mm-aa: ')
    pessoa['cpf'] = input('Digitar cpf: ')

    while ( percorrer_usuarios(usuarios, pessoa) == True):
        print('<< Número de cpf de usuário já cadastrado >>')

        if input('Continuar ou sair da trilha de registrar usuário ? [s/n]: ') == 'n' :
            return usuarios

        pessoa['cpf'] = input('Digitar cpf: ')

    usuarios.append(pessoa)
    
    print('<< Usuário cadastrado com sucesso >>\n')

    print("==========================================")


    return usuarios



def criar_conta(usuarios, contas ):
    
    print("================ CADASTRAR CONTA ================\n")

    #cada conta será um dicionário , e uma chave desse dicionário será 'pessoa' que terá como valor outro dicionário declarado em new_user
    account = dict()
    account['cpf'] = input('Digite cpf do usuário: ')

    while ( encontar_usuarios(usuarios,account) == False ):
        print('\n<< cpf de usuário não encontado  >>\n')

         
        if input('Continuar ou sair da trilha de criar conta ? [s/n]: ') == 'n' :
            return contas

        account['cpf'] = input('Digite cpf do usuário: ')
       

    del account['cpf']
    #após while retornar True , account possui chave 'pessoa'
    account['agencia'] = '001'
    account['position'] = len(contas) + 1
    contas.append(account)

    print('\n<< Conta Registrada com sucesso*** >>\n')

    print("==========================================")


    return contas

    

def listar_contas(contas):
    
    print("================================================================\n")

    for elemento in contas:
        print(f'Agência: {elemento['agencia']}')
        print(f'C/C: {elemento['position']}')
        print(f'Titular : {elemento['pessoa']['nome'] }')
        print

        print("=====================\n")

    print("================================================================\n")


main()




