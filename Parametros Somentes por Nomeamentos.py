def criar_carro(*, modelo, ano, cor, marca, motor, combustivel):
    print(modelo, ano, cor, marca, motor, combustivel)

#criar_carro("Fusca", 1970, "azul",marca="Volkswagen", motor="1.3", combustivel="gasolina") # Invalido # Todos os parâmetros devem ser nomeados

criar_carro(modelo="Fusca", ano=1970, cor="azul", marca="Volkswagen", motor="1.3", combustivel="gasolina") # Valido # Todos os parâmetros devem ser nomeados