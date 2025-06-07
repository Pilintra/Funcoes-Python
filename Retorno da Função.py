def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def fun_3():
    print("Olá mundo!")

# Testando as funções
print(fun_3()) # Saída: None
print(calcular_total([10, 20, 34])) # Saída: 64
print(retornar_antecessor_e_sucessor(10)) # Saída: (9, 11)