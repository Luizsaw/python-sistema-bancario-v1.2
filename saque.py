from transacao import Transacao

class Saque(Transacao):
    def registrar(self, conta):
        if(conta.sacar(self._valor)):
            return True