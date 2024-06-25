menu = """

1) Depositar
2) Sacar
3) Extrato
4) Sair

"""
saldo = 0
limite = 500
extrato = ""
numSaques = 0
LIM_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Coloque o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"

        else:
            print("Operação falha! Valor inválido")

    elif opcao == "2":
        valor = float(input("Qual o valor do saque? : "))

        ex_saldo = valor > saldo
        ex_limite = valor > limite
        ex_saque = numSaques >= LIM_SAQUES

        if ex_saldo:
            print("Operação falha! você não tem saldo suficiente")

        elif ex_limite:
            print("Operação falha! Saque além do limite da conta")

        elif ex_saque:
            print("Operação falha! Saques exedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numSaques += 1

        else:
            print("Operação falha! Valor inválido")


    elif opcao == "3":
        print("Extrato".center(50,"-"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print(50*"-")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, please selecione a opção desejada!")
