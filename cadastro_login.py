menu_incial  = '''
======== AGIOTA 'S COMPANY ========

[c] cadastrar
[k] criar conta - apenas após criar usuário
[l] logar conta - apenas após criar conta
[e] encerrar programa

=> '''

menu_login = '''
======== BEM VINDO ========
[e] extrato
[s] sacar
[d] depósito
[s] sair da conta

'''

def inicio():
    
    usuarios = []
    contas = []

    print(menu_incial,end=' ')
    operation = input()
    while True :
        
        if operation == 'c' :
            usuarios , contas = criar_user(usuarios, contas )

        elif operation == 'l' :
            print('implementar')

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
    account['extrato'] = ''
    


    
    contas.append(account)
    print('<< Conta criada com sucesso ***>>')
    print('\n=========================================================\n')
    
    print(f'conta {usuarios}')

    print(f'conta {account}')
    print(f'contas {contas}')
    
    return contas

inicio()

    

    







        
        


