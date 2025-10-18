class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []  # cada cliente tem sua própria lista de contas

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, valor):
        if not valor:
            raise ValueError("Endereço não pode ser vazio")
        self._endereco = valor

    @property
    def contas(self):
        # retorna cópia para proteger encapsulamento
        return self._contas.copy()

    def adicionar_conta(self, conta):
        self._contas.append(conta)
    

