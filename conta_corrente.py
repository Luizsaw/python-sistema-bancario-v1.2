from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, cliente, agencia, numero, saldo=0.0, limite=500.0, limite_saques=3):
        super().__init__(cliente, agencia, numero, saldo)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0  # contador de saques

    @property
    def limite(self):
        return self._limite

    @property
    def limite_saques(self):
        return self._limite_saques

    @property
    def saques_realizados(self):
        return self._saques_realizados

    def sacar(self, valor):
        try:
            # Se for string, tenta converter (aceita vírgula e ponto)
            if isinstance(valor, str):
                valor = float(valor.replace(',', '.'))
                    
            # Verifica o limite de saque
            if self._saques_realizados >= self._limite_saques:
                print("Número máximo de saques atingido, fim da operação.")
                return False
                
            # Verifica se é um número válido
            if not isinstance(valor, (int, float)) or valor <= 0 or valor > self._saldo or valor > self._limite:
                print("Saldo insuficiente ou valor inválido, fim da operação.")
                return False

            # Saque
            self._saldo -= valor
            self._saques_realizados += 1
            print(f"Saque de R$ {valor:.2f} realizado. Saques restantes: {self._limite_saques - self._saques_realizados}")
            return True

        except ValueError:
            print("Valor incorreto, fim da operação.")
            return False

    
