from transacao import Transacao

class Historico:
    def __init__(self):
        self._transacoes = []  # lista para armazenar transações

    @property
    def transacoes(self):
        # retorna uma cópia para proteger o encapsulamento
        return self._transacoes.copy()

    def adicionar_transacao(self, transacao: Transacao):
        # adiciona a transação à lista com data/hora
        self._transacoes.append(transacao)

    def exibir_historico(self):
        if not self._transacoes:
            print("Nenhuma transação realizada.")
            return
        print("Histórico de Transações:")
        for t in self._transacoes:
            print(f"{t.__class__.__name__} | {t.data} | R$ {t.valor}")
