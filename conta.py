from cliente import Cliente
from historico import Historico


class Conta:
    def __init__(self, cliente: Cliente, agencia:str, numero: int, saldo: float = 0.0):
        self._saldo = saldo
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()  # sempre inicia com histórico novo
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente: Cliente, agencia: str, numero: int):
        conta = cls(cliente=cliente, agencia=agencia, numero=numero)
        cliente.adicionar_conta(conta)
        return conta
                
    def sacar(self, valor):
        if valor <= 0 or valor > self._saldo:
            return False
        self._saldo -= valor
        return True

    def depositar(self, valor):
        try:
            # Se for string, tenta converter (aceita vírgula e ponto)
            if isinstance(valor, str):
                valor = float(valor.replace(',', '.'))

            # Verifica se é um número válido
            if not isinstance(valor, (int, float)) or valor <= 0:
                print("Valor incorreto, fim da operação.")
                return False

            # Depósito
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            return True

        except ValueError:
            print("Valor incorreto, fim da operação.")
            return False
