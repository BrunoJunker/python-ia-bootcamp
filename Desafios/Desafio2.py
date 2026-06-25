valor_compra = float(input("digite o valor da compra: "))
if valor_compra >= 500:
    print("Você ganhou um desconto de 20%!")
    print('Esse é seu valor com desconto:', valor_compra - (valor_compra * 0.20))
elif valor_compra >= 200:
    print("Você ganhou um desconto de 10%!")
    print('Esse é seu valor com desconto:', valor_compra - (valor_compra * 0.10)) 
else:
    print("Você não ganhou desconto!")
    print('Esse é seu valor sem desconto:', valor_compra)
