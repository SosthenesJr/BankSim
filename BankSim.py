MENU = """ 
        BankSim

DIGITE UMA OPÇÃO PARA CONTINUAR

    [d] = depositar
    [s] = sacar
    [e] = extrato
    [q] = sair

 """

saldo = 400
limite = 500
numeros_de_saque = 0
LIMITE_SAQUE = 3
extrato = ""
while True:

    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("Informe valor do deposito:R$ "))
        print("Depósito realizado com sucesso!")

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Operação falhou")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:R$  "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor  > limite
        excedeu_saque = numeros_de_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou você não tem saldo!")
        elif excedeu_limite:
            print("Operação falhou, voce não tem limite!")
        elif excedeu_saque:
            print("Você exedeu o limite diarios de saques!")
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numeros_de_saque += 1
        else:
            print("Operação bloqueada, Digite uma opção valida!")
        print("Saque realizado com sucesso!")
    elif opcao == "e":
      print("\n==========Extrato==========")
      print("Não foram realizadas operações."if not extrato else extrato)
      print(f"\n Saldo: r$ {saldo:.2f}")
      print("===============================")

    elif opcao == "q":
        break

    else:
        print("operação invalida, selecione a opção desejada")

