saldoconta = 0

def contaSenha(agencia,conta,senha):
    print(f"Agencia: {agencia}\n Conta: {conta}\n Senha: {senha}")
    
while True:
    
    menu = input("""********************MENU***********************
    [0]-Abrir uma conta:             
    [1]-Deposito:
    [2]-Saque:
    [3]-Extrato:
    [4]-Sair:
    """)
    
    if menu == "0":
        nomeCliente = str(input("Digite seu nome: "))
        idade = int(input("Informe sua idade: "))
        cpfCliente = input("Digite seu CPF: ")
        cepCliente = input("Digite seu cep: ")
        bairroCliente = input("Informe o bairro onde mora e o número: EX[Bom jesus,165]:\n ")
        cidadeEstadoCliente = str(input("Informe sua cidade e estado: EX[Santos-SP]\n"))
        print("\n")
        print("Dados cadastrados na FourBank,abaixo segue informações da conta: ")
        print(f"\n Nome: {nomeCliente}\n IDADE: {idade}\n CPF: {cpfCliente}\n CEP: {cepCliente}\n BAIRRO: {bairroCliente}\n Cidade/Estado: {cidadeEstadoCliente}\n")
        contaSenha(3001,2002125236,829975)
        print("\n")
        
        

    elif menu == "1":
        Deposito = float(input("Valor a ser depositado: "))
        saldoconta += Deposito
        print(f"Depósito de R${Deposito} realizado com sucesso! Saldo atual: R${saldoconta}")
        

    elif menu == "2":
        Saque = float(input("Digite quanto deseja resgatar: "))
        if Saque > saldoconta:
            print("Valor de saque maior do que saldo total da conta! Tente Novamente!")
        else:
            saldoconta -= Saque
            print(f"Saque de R${Saque} realizado. Saldo atual: R${saldoconta}")

    elif menu == "3":
        print(f"Saldo atual da conta: R${saldoconta}")
        break

    elif menu == "4":
        print("Operação Encerrada!")
        break

    else:
        print("Operação inválida!")
        break






   



