from classes import Funcionario_Comissionado, Funcionario_Assalariado

fc1 = Funcionario_Comissionado('Ryan', 50000, 17)

fa1 = Funcionario_Assalariado('Carlos', 20000)

print(f'Nome: {fc1.nome}, Salário: {fc1.salario}, Bonificação: {fc1.calcular_bonificação()}.')

print(f'Nome: {fa1.nome}, Salário: {fa1.salario}, Bonificação: {fa1.calcular_bonificação()}.')