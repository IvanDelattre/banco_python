menu_incial  = '''
=============== AGIOTA 'S COMPANY ===============

[c] cadastrar
[k] criar conta - apenas após criar usuário
[l] logar conta - apenas após criar conta
[e] encerrar programa

=> '''



usuarios = []
contas = []


def inicio(usuarios,contas):
    
    print(menu_incial,end=' ')
    operation = input()
    while True :
        
        if operation == 'c' :
            usuarios , contas = criar_user(usuarios, contas )

        elif operation == 'l' :
            contas = login_incio(contas)

        elif operation == 'c' :
            print('implementar')

        elif operation == 'k':
            contas = criar_conta(contas, usuarios )

        elif operation == 'e' :
            print('\n<< ENCERRADO >>\n ')
            break;
    
        else:
            print("\n <<*** Operação ínvalida ***>>\n ")

        print(menu_incial,end=' ')
        operation = input()    


def percorrer_usuario(usuarios, user):
    for elemento in usuarios :
        if elemento['cpf'] == user['cpf']:
            return True
    return False


def encontar_usuario(usuarios , account ):
    account['nome'] = account['nome'].strip()
    for elemento in usuarios:
        if elemento['nome'] == account['nome']:
            account['pessoa'] = elemento
            return True
    return False


def criar_user(usuarios, contas):
    print('\n====================== CRIAR USUÁRIO ======================\n')
    
    user = dict()
    user['nome'] = input('Digite nome completo: ')
    user['cpf'] = input('Digite CPF : ')

    while(percorrer_usuario(usuarios,user) == True):
        print('\n<< Esse CPF já foi registrado >>\n')

        if ( input('Continuar com a trilha de criar usuário? [s/n]') == 'n'):
            return usuarios , contas
        
        user['cpf'] = input('Digite CPF : ')
    
    usuarios.append(user)
    print('<< Usuário cadastrado com sucesso ***>>')
    print('\n============================================================\n')


    if ( input('Continuar criação da conta : [s/n] ')== 'n'):
        return usuarios  , contas
    
    contas = criar_conta(contas,usuarios)
    

    return usuarios, contas


def criar_conta(contas, usuarios):
    print('\n====================== CRIAR CONTA ======================\n')

    account = dict()
    account['nome'] = input('Digite nome completo do úsuario : ')
    while encontar_usuario(usuarios, account ) == False:
        print('\n<< Esse nome não foi registrado  >>\n')

        if ( input('Continuar com a trilha de criar conta ? [s/n]') == 'n'):
            return contas

        account['nome'] = input('Digite nome completo do úsuario : ')

    #depois da função encontar usuário retornar 'True' account possui chaave 'pessoa' que tem como valor outro dicionário chamado
    del account['nome']
    account['senha'] = input('Difinir senha: ')
    #implementar comparador de senha

    

    account['position'] = len(contas) + 1
    account['saldo'] = 0
    account['extrato'] = ''
    


    
    contas.append(account)
    print('<< Conta criada com sucesso ***>>')
    print('\n=========================================================\n')
    
    print(f'conta {usuarios}')

    print(f'conta {account}')
    print(f'contas {contas}')
    
    return contas


def encontrar_conta(contas, account):
    for elemento in contas:

        if elemento['pessoa']['nome'] == account['nome']:
            
            account['conta'] = elemento  


            return True
    return False



def login_incio(contas):
    print('\n====================== Login  ======================\n')
    account = dict()
    account['nome'] = input('Digite Nome completo do usuário: ')
    account['nome'] = account['nome'].strip()
    #se nome usuário  não for encontado
    while encontrar_conta(contas, account) == False :
        print('\n<< Usuário não encontrado >>>\n')
        if ( input('Continuar com a trilha de Login? [s/n]') == 'n'):
            inicio()
        account['nome'] = input('Digite Nome completo do usuário: ')

    del account['nome']
    cliente = account['conta'].copy()
    

    senha = input(f'Digite senha de {cliente['pessoa']['nome'] } :')
    
    while senha != cliente['senha'] :

        print('\n<< @@Senha Incorreta ***>>\n')
        decision = input(f'''Opções :
        - sair da trilha de login [n]
        - trocar de usuário atual : {cliente['pessoa']['nome']} [l]
        - continuar no usuário atual [s] => ''')
        if decision == 'n':
            inicio()
        elif decision == 'l':
            login_incio(contas)
        
        senha = input(f'Digite senha de {cliente['pessoa']['nome'] } :')

    #a partir desse bloco de código a senha está correta
    print('\n<<< Perfil Logado ***>>>\n')


    print('\n====================================================\n')
    contas = interface_perfil(cliente,contas)

    return contas



def interface_perfil(cliente, contas):
    account = dict()
    for elemento in contas :
        if cliente['pessoa']['nome'] == elemento['pessoa']['nome']:
            account = elemento


    menu_login = f'''
=============== Bem Vindo {cliente['pessoa']['nome']} ===============
[e] extrato
[s] sacar
[d] depósito
[sa] sair da conta
[i] informações da conta
=>'''
    print(menu_login,end=' ')
    op = input()
    while True :

        if op == 'e':
            extrato(account)

        elif op == 's':
            account = saque(account)

        elif op == 'd':
            depositar(account)

        elif op == 'sa':
            print('<< Saindo da Conta ***>>')
            break

        elif op == 'i':
            info_conta(account)
        else:
            print('<< OPERAÇÃO INVÁLIDA >>')

        print(menu_login)
        op = input()
    
    print('=========== ======================================== ===========')

    return contas 



def depositar(account):
    print('\n==================== Depósito ====================\n')

    deposito = float(input('Digite valor do depósito: R$ '))
    account['saldo'] += deposito

    account['extrato'] += f'Depósito de R${deposito}\n'

    print('\n<<< Depósito Realizado com sucesso ****>>>\n' )

    print('==================== ======== ==================== ')




def info_conta(account):
    print('\n====================_DADOS_CONTA_====================\n')

    print(f'Nome Usuário : {account['pessoa']['nome']}')

    print(f'CPF do usuário: {account['pessoa']['cpf'] }')

    print(f'Numéro da conta: {account['position']}')

    print(f'Conta corrente : {account['saldo']}')

    print('\n=====================================================\n')


def extrato(account):
    print('\n==================== Extrato ====================\n')
    print('Registro de operações:')
    print(account['extrato'])

    print(f'Saldo Final : R${account['saldo']}')

    print('\n==================== ======= ====================\n')


def saque(account):
    saque = float(input('Digite Valor de Saque R$ '))

    if saque > account['saldo']:
        print('<< Valor de saque Não dispónivel na conta >>>')
        print(f'Saldo na conta: {account['saldo']}\n' )
        return account 
    account['saldo'] -= saque
    account['extrato'] += f'Saque realizado no valor de R${saque}'

    return account




inicio(usuarios, contas)




    

    







        
        


