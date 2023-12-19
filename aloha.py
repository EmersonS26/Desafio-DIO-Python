saldoconta = 0

while True:
    menu = input("""********************MENU***********************
    [1]-Deposito
    [2]-Saque
    [3]-Extrato
    [4]-Sair
    """)

    if menu == "1":
        Deposito = float(input("Valor a ser depositado: "))
        saldoconta += Deposito
        print(f"Depósito de R${Deposito} realizado. Saldo atual: R${saldoconta}")
        

    elif menu == "2":
        Saque = float(input("Digite quanto deseja resgatar: "))
        if Saque > saldoconta:
            print("Valor de saque maior do que saldo total da conta! Tente Novamente!")
        else:
            saldoconta -= Saque
            print(f"Saque de R${Saque} realizado. Saldo atual: R${saldoconta}")

    elif menu == "3":
        print(f"Saldo atual da conta: R${saldoconta}")

    elif menu == "4":
        print("Operação Encerrada!")
        break

    else:
        print("Operação inválida!")
