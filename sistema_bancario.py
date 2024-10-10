MENU = """
Selecione a opção que deseja:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato= ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao =="d":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R$ {valor:.2f} \n"

        else:
            print("\nOperação falhou! Por favor digite um valor valido.")


    elif opcao == "s":
        valor = float(input("\nDigite o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_limite_saque = numero_saques>= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Saldo insuficiente.")
            print(f"\nSeu saldo é de: R${saldo:.2f}")

        elif excedeu_limite:
            print("\nOperação falhou! Você excedeu seu limite de saque.")
            print(f"\nSeu limite é de saque é de: R${limite:.2f}")

        elif excedeu_limite_saque:
            print("\nOperação falhou! Você excedeu seu limite diario de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R${valor:.2f}\n"
            numero_saques += 1 

        else:
            print("\nOperação falhou! Por favor digite um valor valido.") 



    elif opcao =="e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação invalida! Por favor selecione novamente a opção desejada")

    