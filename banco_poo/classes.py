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



def main():
    clientes = []
    contas = []
    print(menu,end='')
    
    while True:
        opcao = input()

        if opcao == "d":
            pass
            #implementar

        elif opcao == "s":
            pass
            #implementar

        elif opcao == "e":
            pass
            #implementar


        elif opcao == "nu":
            pass
            #implementar


        elif opcao == "nc":
            pass
            #implementar


        elif opcao == "lc":
            pass
            #implementar


        elif opcao == "q":
            pass
            #implementar


        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")
        
        print(menu,end='')

main()