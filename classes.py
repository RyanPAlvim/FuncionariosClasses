from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    @abstractmethod
    def calcular_bonificação(self):
        ...

class Funcionario_Comissionado(Funcionario):
    def __init__(self, nome: str, salario: float, percentual_comissão: int):
        super().__init__(nome, salario)
        self.percentual_comissão = percentual_comissão

    def calcular_bonificação(self):
        return self.salario * (self.percentual_comissão/100)
    
class Funcionario_Assalariado(Funcionario):
    def __init__(self, nome: str, salario: float):
        super().__init__(nome, salario)

    def calcular_bonificação(self):
        return self.salario * 0.1

