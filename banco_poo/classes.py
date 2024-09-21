from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
    def __init__(self):
        self.contas = []


class Pessoa(Cliente):
    def __init__(self, cpf , nome , data):
        super().__init__()
        self.cpf = cpf
        self.nome = nome
        self.data = data

class Conta:
    def __init__(self, cliente):
        self.saldo = 0
        self.numero = 0 
        self.cliente = cliente
        self.limite_saques = 3

    def deposito(self, valor):
        self.saldo += valor
        

    def saque(self , valor):
        if self.saldo > 500 and valor <=500 and self.limite_saques > 0:
            self.limite_saques -= 1
            self.saldo -= valor
            return True
        print('Error@@@ Limite de condições de saque já atingidas  ')
        return False 

        


class ContaCorrente(Conta):
    def __init__(self, cliente, historico):
        super().__init__(cliente, historico)
        self.limite = 500
        self.limite_saques = 3


class Transacao(ABC):
    
    @abstractclassmethod
    def registrar(self,conta):
        pass


class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor


class Deposito(Transacao):

    def __init__(self, valor ):
        super().__init__()
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    


menu = """\n
    ================ MENU ================
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [nc]Nova conta
    [lc]Listar contas
    [nu]Novo usuário
    [q]Sair
    => """



def novo_usuario(lista_clientes):
    
    cpf = input('Informe o CPF: ')

    for i in range(len(lista_clientes)):
        if lista_clientes[i].cpf == cpf:
            print(' ERror @@@: CPF já existente na Lista')
            return lista_clientes

    nome = input('Informe o nome: ')
    data = input('Informe Data: ')
    pessoa = Pessoa(cpf, nome, data)

    lista_clientes.append(pessoa)

    return lista_clientes


def nova_conta(lista_clientes, lista_contas):
    cpf_procurado = input('Digite CPF do Cliente: ')
    for i in range(len(lista_clientes)):
        if lista_clientes[i].cpf == cpf_procurado:
            conta = Conta(lista_clientes[i])
            conta.numero = len(lista_contas) + 1
            lista_clientes[i].contas.append(conta)
            lista_contas.append(conta)

            #for conta in lista_clientes[i].contas:
                #print(conta.numero)


            print('Conta cadastrasa com sucesso!!!')
            return lista_clientes, lista_contas

    print('ERroR @@@CPF não encontrado na lista de usuários')
    return lista_clientes, lista_contas


def listar_contas(lista_contas):
    
    print('---------------------------------------')
    for elemento in lista_contas:

        print(f'Nome: {elemento.cliente.nome}')
        print(f'CPF: {elemento.cliente.cpf}')
        print(f'Data nascimento: {elemento.cliente.data}')
        print(f'Saldo bancário: {elemento.saldo}')
        print(f'Número Conta: {elemento.numero}')

        print('---------------------------------------')

def depositar_valor(lista_clientes):
    cpf_procurado = input('Informe CPF da conta da qual se deseja depositar: ')

    for elemento in lista_clientes:
        if elemento.cpf == cpf_procurado:
            
            numero_conta = int(input('Digite Número da conta de depósito: ') )
            
            for conta in elemento.contas:

                if conta.numero == numero_conta:
                    deposito = float(input('Digite valor que se queira depositar: ') )
                    conta.deposito(deposito)
                    print('Depósito realizado com sucesso!!\n')

                    return lista_clientes
            print('ErRoR @@ número de conta não encontrado')
            return lista_clientes    
            
    print('ERror@@ cpf não encontrado')
    return lista_clientes



def sacar_valor(lista_clientes):
    cpf_procurado = input('Informe CPF da conta da qual se deseja sacar: ')

    for elemento in lista_clientes:
        if elemento.cpf == cpf_procurado:
        
            numero_conta = int(input('Digite Número da conta de saque: ') )
            
            for conta in elemento.contas:

                if conta.numero == numero_conta:
                    valor = float(input('Digite valor que se queira sacar: ') )
                    
                    if conta.saque(valor) == False:
                        return lista_clientes



                    print('Saque realizado com sucesso!!\n')

                    return lista_clientes
            print('ErRoR @@ número de conta não encontrado')
            return lista_clientes    
            
    print('ERror@@ cpf não encontrado')
    return lista_clientes

def main():
    lista_clientes = []
    lista_contas = []
    print(menu,end='')
    
    while True:
        opcao = input()

        if opcao == "d":
            lista_clientes = depositar_valor(lista_clientes)

        elif opcao == "s":
            lista_clientes = sacar_valor(lista_clientes)

        elif opcao == "e":
            pass

        elif opcao == "nu":
            pass
            lista_clientes = novo_usuario(lista_clientes)



        elif opcao == "nc":
            lista_clientes, lista_contas = nova_conta(lista_clientes, lista_contas)


        elif opcao == "lc":
            listar_contas(lista_contas)


        elif opcao == "q":
            print('Bye, Baby, Bye Bye!!')
            break


        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
        
        print(menu,end='')

main()

