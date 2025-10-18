from transacao import Transacao

class Deposito(Transacao):
    def executar(self, conta):
        if(conta.depositar(self._valor)):
            return True