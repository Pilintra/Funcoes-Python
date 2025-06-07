def salvar_carro(marca, modelo, ano, placa):
    # Função para salvar os dados do carro
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Chamadas da função fora da definição para evitar recursão
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Carro inserido com sucesso! Fiat/Palio/1999/ABC-1234