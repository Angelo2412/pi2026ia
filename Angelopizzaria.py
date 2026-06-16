pizzas = {
    "Calabresa":{"P":35.00,"M":45.00,"G":55.00},
    "Mussarela":{"P":33.00,"M":43.00,"G":53.00},
    "Frango com catupiry":{"P":38.00,"M":48.00,"G":58.00},
    "Portuguesa":{"P":40.00,"M":50.00,"G":60.00},
    "Bacon com milho":{"P":40.00,"M":50.00,"G":60.00},
    "Quatro queijo":{"P":40.00,"M":50.00,"G":60.00},
    "Coração":{"P":45.00,"M":57.00,"G":70.00},
    "Strogonoff":{"P":55.00,"M":60.00,"G":80.00}
}

print(f"{'Sabor':<22} {'P':<8} {'M':<8} {'G':<8}")
print("-" * 50)

for sabor, tamanhos in pizzas.items():
    print(f"{sabor:<22} {tamanhos['P']:<8.2f} {tamanhos['M']:<8.2f} {tamanhos['G']:<8.2f}")

while True:
    sabor = input("\nDigite o sabor da pizza (ou exit para sair): ")

    if sabor.lower() == "exit":
        print("Programa encerrado.")
        break

    if sabor not in pizzas:
        print("Sabor não encontrado!")
        continue

    tamanho = input("Digite o tamanho (P, M ou G): ").upper()

    if tamanho not in pizzas[sabor]:
        print("Tamanho inválido!")
        continue

    valor = pizzas[sabor][tamanho]
    print(f"Pedido: {sabor} ({tamanho}) - R$ {valor:.2f}")
    




    print(f"{'Sabor':<22} {'P':<8} {'M':<8} {'G'}")
print("-" * 50)

for sabor, tamanhos in pizzas.items():
    print(f"{sabor:<22} {tamanhos['P']:<8.2f} {tamanhos['M']:<8.2f} {tamanhos['G']:.2f}")