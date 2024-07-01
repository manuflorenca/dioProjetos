import textwrap


def menu():
    menu = """\n

    ========Menu========

    1)\t Depositar
    2)\t Sacar
    3)\t Extrato
    4)\t Nova conta
    5)\t Listar contas
    6)\t Novo usuário
    7)\t Sair

    -> """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t R$ {valor:.2f}\n"
        print("\n Depósito reaizado com sucesso!!!")
    else:
        print("\n Operação falha! Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numSaques, limite_saques):

    ex_saldo = valor > saldo
    ex_limite = valor > limite
    ex_saques = numSaques >= limite_saques

    if ex_saldo:
        print("\n Operação falhou! Saldo insuficiente.")

    elif ex_limite:
        print("\n Operacão falhou! Saque excede limite.")

    elif ex_saques:
        print("\n Numero de saques exedidos")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t R$ {valor:.2f}\n"
        numSaques += 1
        print("\n Saque realizado com sucesso!")

    else:
        print("\n Operação falhou! Valor inválido.")

    return saldo, extrato, numSaques


def exibibir_extrato(saldo, /, *, extrato):
    print("Extrato".center(50, "-"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print(50 * "-")


def criar_usuario(usuarios):
    cpf = input(" Informe o CPF (somente o número): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF! ")
        return
    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(" Informe o endereço (logradouro - nro - bairro - cidade/sigla estado")

    usuarios.append({"nome:", nome, "data_nascimento:", data_nascimento, "cpf", cpf, "endereco:", endereco})
    print("Usuário criado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrada!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C\C:\t\t {conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}    
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIM_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numSaques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Coloque o valor do depósito:"))

            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R${valor:.2f}\n"

            else:
                print("Operação falha! Valor inválido")

        elif opcao == "2":
            valor = float(input("Qual o valor do saque? : "))

            saldo, extrato, numSaques = sacar(

                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numSaques=numSaques,
                limite_saques=LIM_SAQUES,
            )

        elif opcao == "3":
            exibibir_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)


        elif opcao == "7":
            break

        else:
            print("Operação inválida, please selecione a opção desejada!")


main()
