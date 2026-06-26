repetir = "s"
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
print("A soma dos numeros é: ",(numero1 + numero2))
repetir = input(" Deseja realizar outro calculo? (s/n) ").lower()
while repetir == "s":
    
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    print("A soma dos numeros é: ",(numero1 + numero2))
    repetir = input(" Deseja realizar outro calculo? (s/n) ").lower()
print("programa encerrado")