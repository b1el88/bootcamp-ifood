menu = """
========== MENU ==========

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==========================
=> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        deposito = float(input("Informe o valor a ser depositado: R$ "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito de R$ {deposito:.2f} \n"
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!")

        else:
            print("Valor inválido.")
    
    elif opcao.lower() == "s":
        saque = float(input("Informe o valor a ser sacado: R$ "))

        if saque > limite:
            print(f"O limite para cada saque é de R$ {limite}")
        
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Você já realizou um total de {LIMITE_SAQUES} saques diários.")
        
        elif saque > saldo:
            print("Saldo insuficiente!")

        elif saque < 0:
            print("Valor inválido.")

        else:
            numero_saques += 1
            saldo -= saque
            extrato += f"Saque de R$ {saque:.2f} \n"
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        

    elif opcao.lower() == "e":
        if bool(extrato)  == True:
            print("========= EXTRATO =========")
            print(extrato)
            print(f"Seu saldo é de R$ {saldo:.2f}")
            print("===========================\n")

        else:
            print("Não foram realizadas movimentações.")  

    elif opcao.lower() == "q":
        print("Encerrando o programa[...]")
        break 
    
    else:
        print("Operação inválida, selecione novamente a operação desejada: ")