# PARADIGMA ORIENTAÇÃO A OBJETOS

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():  # static method (não precisa do self, não precisa do objeto
        return 'BB 001'  # No exercício só estamos trabalhando com o BB:001...

    @staticmethod
    def codigos_bancos(): #static method (não precisa do self, não precisa do objeto
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}

    def extrato(self):
        print("Saldo de {}, do titular {}.".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        print("Houve um depósito de {}.".format(valor))

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("Houve um saque de {}.".format(valor))

        else:
            print("Você não tem limite para este saque.")

    def transfere(self, valor, destino):
        self.saca(valor), print("da conta do {}.".format(self.__titular))
        destino.deposita(valor), print("para a conta do {}.".format(destino.__titular))


# codigo = Conta.codigo_banco()
# codigos = Conta.codigos_bancos()

conta = Conta(123, "Nico", 55.0, 1000.0)


print("...........................")

print(conta.extrato())

print(conta.deposita(15.0))
print(conta.extrato())

print(conta.saca(1010))
print(conta.extrato())

print(conta2.transfere(10.0, conta))
print(conta2.extrato())
print(conta.extrato())

print(conta.saldo)

# print(codigo)
# print(codigos)
# print(codigos['Bradesco'])
