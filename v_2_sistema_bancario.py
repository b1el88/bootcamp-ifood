menu = """
========== MENU ==========

[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[l] Listar contas
[q] Sair

==========================
=> """


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f} \n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    else:
        print("Falha: valor inválido.")
    
    return saldo, extrato

def sacar(*, valor, limite, numero_saques, saldo, extrato, limite_saques):
    if valor > limite:
        print(f"Falha: o limite para cada saque é de R$ {limite}")
        
    elif numero_saques >= limite_saques:
        print(f"Falha: você já realizou um total de {limite_saques} saques diários.")
        
    elif valor > saldo:
       print("Falha: saldo insuficiente!")

    elif valor < 0:
     print("Falha: valor inválido.")

    else:
        numero_saques += 1
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f} \n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques

def tirar_extrato(saldo, /, *, extrato):
    if extrato:
        print("========= EXTRATO =========")
        print(extrato)
        print(f"Seu saldo é de R$ {saldo:.2f}")
        print("===========================\n")

    else:
        print("Não foram realizadas movimentações.") 
        
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print(linha)

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    numero_saques = 0
    limite = 500
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao.lower() == "d":
            valor = float(input("Informe o valor a ser depositado: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao.lower() == "s":
            valor = float(input("Informe o valor a ser sacado: R$ "))

            saldo, extrato, numero_saques = sacar(
                valor=valor,
                saldo=saldo, 
                limite=limite,
                numero_saques=numero_saques,
                extrato=extrato,
                limite_saques=LIMITE_SAQUES
            )
     
        elif opcao.lower() == "e":
            tirar_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)


        elif opcao.lower() == "q":
            print("Encerrando o programa[...]")
            break 
    
        else:
            print("Operação inválida, selecione novamente a operação desejada: ")

main()