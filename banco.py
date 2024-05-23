class Banco:

    LIMITE_DE_SAQUE_DIARIO = 3
    SOMA_DE_SAQUES_DIARIO = 500.0
    LISTA_DE_SAQUES = []

    def __init__(self, saldo):
        self.saldo = saldo

    def deposito(self, deposito):
        self.saldo += float(deposito)
        self.extrato()

    def saque(self, valor):
        if self.saldo < valor:
            print("\nNao foi possivel sacar saldo insuficiente")
            self.extrato()
        else:
            self.LISTA_DE_SAQUES.append(valor)
            operacao = self.saldo - valor
            print("Valor sacado : ", valor)
            self.saldo = operacao
            self.extrato()

    def extrato(self):
        soma_saldo = self.saldo
        if  soma_saldo == 0:
            print("-----------------------\n")
            print("\nSaldo da conta zerado R$ {:.2f}\n".format(self.saldo))
            print("-----------------------")

        else:
            print("-----------------------\n")
            print("Imprimindo extrato: R$ {:.2f}\n".format(self.saldo))
            print("-----------------------")


    def limite (self, soma_dos_saques, quantidade_saques_diarios):
        if quantidade_saques_diarios >= self.LIMITE_DE_SAQUE_DIARIO:
            if soma_dos_saques == self.LIMITE_DE_SAQUE_DIARIO:
                print(f"\nVoce atingiu o limite de '{self.LIMITE_DE_SAQUE_DIARIO}' saques diarios ")
                return True
            elif soma_dos_saques >= self.SOMA_DE_SAQUES_DIARIO :
                print("A soma de saques diarios chegou no seu limite de: ", self.SOMA_DE_SAQUES_DIARIO)
                return True
            else:
                False

    def impressao_de_saques (self):
        index = 1 
        print("Saques efetuados no dia\n")
        for lista in self.LISTA_DE_SAQUES:
            print("O "+ str(index) +"º saque foi de: "+ "R$ {:.2f}".format(lista))
            index += 1