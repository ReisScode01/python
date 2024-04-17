peso=float(input("Digite seu peso: "))
altura=float(input("Digite sua altura em metros: "))
imc=(peso/(altura**2))

if imc <0:
    print("Insira um valor válido")
    

else:
    if imc <=18.5: 
        print("Abaixo do peso")
    elif imc >=18.5 and imc <24.9:
        print("Peso Normal")
    elif imc >=25.0 and imc <29.9:
        print("Sobrepeso")
    elif imc >=30.0 and imc <34.9:
        print("Obesidade Grau I")
    elif imc >=35.0 and imc <39.9:
        print("Obesidade Grau II (severa)")
    else:
        print("Obesidade Grau III (mórbida)")
