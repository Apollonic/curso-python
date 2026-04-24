pequeno = 10
medio = 20
grande = 30

print("-"*10)
print("pequeno = 10\nmédio = 20 \ngrande = 30")
print("-"*10)
milk = input("qual tamanho de milkshake você quer? ").lower()
quant = int(input("quantos quer? "))
if milk == "pequeno":
    custo = quant*pequeno
elif milk == "medio":
    custo = quant*medio
elif milk == "grande":
    custo = quant*grande
else:
    print("valor inválido")
    custo = 0

print("seu pedido custou: {}".format(custo))
