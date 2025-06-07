salario = 2000

def calcular_bonus(salario):
    bonus = salario * 0.1  # exemplo de cálculo de bônus de 10%
    return salario + bonus

calcular_bonus(500)
print(salario + calcular_bonus(500))  # imprime 2550
print(salario)  # imprime 2000

# # O código abaixo não funciona porque a variável salario é global, mas não é declarada como global dentro da função.
# salario = 2000
# def salario_bonus(bonus):
#     global salario
#     salario += bonus
#     return salario

# salario_bonus(500)