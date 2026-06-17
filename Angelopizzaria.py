pizzas = {
    "Calabresa": {"Pequeno": 35.00, "Media": 45.00, "Grande": 55.00},
    "Mussarela": {"Pequeno": 33.00, "Media": 43.00, "Grande": 53.00},
    "Frango com catupiry": {"Pequeno": 38.00, "Media": 48.00, "Grande": 58.00},
    "Portuguesa": {"Pequeno": 40.00, "Media": 50.00, "Grande": 60.00},
    "Bacon com milho": {"Pequeno": 40.00, "Media": 50.00, "Grande": 60.00},
    "Quatro queijo": {"Pequeno": 40.00, "Media": 50.00, "Grande": 60.00},
    "Coração": {"Pequeno": 45.00, "Media": 57.00, "Grande": 70.00},
    "Strogonoff": {"Pequeno": 55.00, "Media": 60.00, "Grande": 80.00}
}

while True:
    sabor = input("Digite o sabor  (ou 'exit' para sair): ").title()

    if sabor.lower() == "exit":
        print("Programa encerrado.")
        break

    if sabor not in pizzas:
        print("Não tem o sabor!")
        continue

    tamanho = input("Digite o tamanho (Pequeno, Media ou Grande): ").title()

    if tamanho not in pizzas[sabor]:
        print("Tamanho inválido!")
        continue

    valor = pizzas[sabor][tamanho]

    print(f"\nPedido: {sabor} ({tamanho})")
    print(f"Valor: R$ {valor:.2f}\n")