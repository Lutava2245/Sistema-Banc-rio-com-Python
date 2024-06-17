saldo = 0
operacao = -1
extrato = ""

total_deposito = 0
quant_deposito = 0

total_saque = 0
quant_saque = 0

while operacao != 0:

    operacao = int(input(f"""
====MENU====       
1 - Depósito
2 - Saque
3 - Extrato
                        
0 - Sair
============
"""))
    
    if operacao == 1:
        deposito = float(input("Valor a Depositar: "))
        while deposito < 0:
            deposito = float(input("Não pode ser menor que 0: "))
        
        if deposito != 0:
            saldo += deposito
            extrato += f"\nDepositou R$ {deposito:.2f}"
            total_deposito += deposito
            quant_deposito += 1

    elif operacao == 2:
        if quant_saque == 3:
            print("Limite diário de Saques excedido:", 3)

        else:
            saque = float(input("Valor a sacar: "))
            while saque < 0 or saque > 500:
                saque = float(input("R$ 500.00 é o valor máximo para saques\nO valor não pode ser menor que 0: "))
            
            if saldo < saque:
                print("Saldo Insuficiente.")
            elif saque != 0:
                saldo -= saque
                extrato += f"\nSacou R$ {saque:.2f}"
                total_saque += saque
                quant_saque += 1
            
    elif operacao == 3:
        print("===========EXTRATO===========", end="")

        print("\nNada foi feito." if extrato == "" else extrato)
        print(f"""=============================
Nº Depósitos: {quant_deposito}
Total Depositado: R$ {total_deposito:.2f}
=============================
Nº Saques: {quant_saque}
Total Sacado: R$ {total_saque:.2f}
=============================""")
        
        print(f"Saldo: R$ {saldo:.2f}")
        
    elif operacao == 0:
        print("Obrigado por usar o programa!")
    else: print("Escolha uma das opções válidas.")