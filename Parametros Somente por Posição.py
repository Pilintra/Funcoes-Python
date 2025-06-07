def criar_carro(modelo, ano, cor, /, *, marca, motor, combustivel):
    print(modelo, ano, cor, marca, motor, combustivel)

# Exemplo de chamada da função
# criar_carro("Fusca", 1970, "azul", "Volkswagen", "1.3", "gasolina") Invalido: parâmetros após '/' devem ser nomeados

criar_carro("Fusca", 1970, "azul", marca="Volkswagen", motor="1.3", combustivel="gasolina")  # Correto: parâmetros antes de '/' são apenas posicionais


