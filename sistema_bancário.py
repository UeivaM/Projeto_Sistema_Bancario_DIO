def depositar(saldo, extrato):
  print("Depósito")
  deposito = float(input("Informe quanto deseja depositar: "))
  saldo = saldo + deposito
  extrato = extrato + "\n deposito: R$" + str(deposito)
  print("Depósito realizado com sucesso!")
  return saldo, extrato

def sacar (saldo, extrato, numero_saques, limite_saques):
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
  return saldo, extrato

def extrato_bancario (saldo, extrato):
  print("Extrato")
  extrato = extrato + "\n" + "saldo: " + str(saldo)
  print(extrato)

  return saldo, extrato


def verificar_cpf_existente(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario['CPF'] == cpf:
            return True
    return False

def verificar_usuario(lista_usuarios, cpf):
    for usuario in lista_usuarios:
        if usuario['CPF'] == int(cpf):
            return usuario
    return None

def cadastrar_usuario(lista_usuarios):
    cpf = int(input("Insira o seu CPF (somente números):"))

    if verificar_cpf_existente(lista_usuarios, cpf):
        print("Usuário já cadastrado")
    else:
        nome = input("Insira o seu nome completo: ")
        nascimento = input("Insira a sua data de nascimento (dd/mm/aaaa): ")
        endereco = input("Insira o seu endereço (logradouro, nº, bairro, cidade/sigla): ")

        lista_usuarios.append({'CPF': cpf, 'NOME': nome, 'Data de nascimento': nascimento, "Endereço": endereco})
        print("Usuário cadastrado com sucesso!")
      
    return lista_usuarios

def criar_conta(agencia, lista_usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = verificar_usuario(lista_usuarios, cpf)

    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": agencia, "numero da conta": numero_conta, "usuário": usuario['NOME']}
        contas.append(conta)
        print("Conta criada com sucesso para o usuário:", usuario['NOME'])
    else:
        print("ERRO: Usuário não encontrado!")

    return contas

menu = """
Precione:
[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar Usuário
[c] Criar Conta
[w] print usuarios
[pc] print conta
[q] Sair

=>"""

saldo  = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
i = 1
lista_usuarios = []
agencia = "0001"
contas = []

while True:

    opcao = input(menu)

    if opcao == "d":
      saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
      saldo, extrato = sacar(saldo, extrato, numero_saques, limite_saques)

    elif opcao == "e":
      extrato_bancario(saldo, extrato)

    elif opcao == "u":
      cadastrar_usuario(lista_usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        contas = criar_conta(agencia, lista_usuarios, contas)

    elif opcao == "q":
        break
    
    elif opcao == "w":
      print(lista_usuarios)

    elif opcao == "pc":
      print(contas)


    else:
        print("Operação inválida. Selecione novamente a operação desejada.")

print("O BancoX agradece!")