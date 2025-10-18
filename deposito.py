from transacao import Transacao

class Deposito(Transacao):
    def registrar(self, conta):
        if(conta.depositar(self._valor)):
            return True