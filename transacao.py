from abc import ABC, abstractmethod
from datetime import datetime

class Transacao(ABC):
    def __init__(self, valor: float, data: datetime = None):
        self._valor = valor
        self._data = data or datetime.now()

    @property
    def valor(self):
        return self._valor
    
    @property
    def data(self):
        return self._data

    @abstractmethod
    def executar(self, conta):
        pass
