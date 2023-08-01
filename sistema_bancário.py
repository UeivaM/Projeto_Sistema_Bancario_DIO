menu = """
Precione:  
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo  = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
i = 1

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Depósito")
        deposito = float(input("Informe quanto deseja depositar: "))
        saldo = saldo + deposito
        extrato = extrato + "\n deposito: R$" + str(deposito)
        print("Depósito realizado com sucesso!")
    
    elif opcao == "s":
        print("Saque")
        
        if numero_saques <= limite_saques:
            
            saque= float(input("Informe quanto deseja sacar: "))
                               
            if saque <= saldo:
                    saldo = saldo - saque
                    extrato = extrato + "\n saque: R$" + str(saque)
                    print("Saque realizado com sucesso!")
                    limite_saques = limite_saques - 1
                    numero_saques =+ 1
                        
            else:
                print("Saldo insuficiente.")
            
        else:
                print("Limite de saque atingido.")
         
    elif opcao == "e":
        print("Extrato")
        extrato = extrato + "\n" + "saldo: " + str(saldo)
        print(extrato)

    elif opcao == "q":
        break
    
    else:
        print("Operação inválida. Selecione novamente a operação desejada.")
    
print("O BancoX agradece!")