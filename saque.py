from transacao import Transacao

class Saque(Transacao):
    def executar(self, conta):
        if(conta.sacar(self._valor)):
            return True