from banco import Banco

usuario_cadastrado = "vitor"

banco = Banco(0)
usuario = input("Digite o seu nome: ")
limite_de_saque = 500.0
quantidade_saques_diarios = 0
soma_dos_saques = 0

if (usuario.lower() != usuario_cadastrado.lower()):
    print("Usuario nao encontrado!")
else: 
    
    while True:

        opcao = int(input("Digite a funcionalidade que deseja:\n \n [1] - Deposito\n [2] - Sacar \n [3] - Extrato \n [0] - para sair: "))
        if(opcao == 1):
            valor = input("Digite o valor a ser depositado: ")
            banco.deposito(valor)
            continue

        if (opcao == 2):
            if soma_dos_saques >= banco.SOMA_DE_SAQUES_DIARIO or quantidade_saques_diarios >= banco.LIMITE_DE_SAQUE_DIARIO:
                print("\nvoce atingiu o limite de 3 saques diarios")
                banco.extrato()
                banco.impressao_de_saques()
                break
            else: valor = float(input("Digite o valor a ser sacado: "))
            print()
            banco.saque(valor)
            soma_dos_saques += valor
            quantidade_saques_diarios += 1
            if banco.limite(soma_dos_saques, quantidade_saques_diarios) == True:
                break
            continue

        if (opcao == 3):
            banco.extrato()
            continue
        else:
            break
