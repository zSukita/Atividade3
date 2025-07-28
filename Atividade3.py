# 1 - CLASSIFICADOR DE IDADE
def classificador_idade():
    print("=== CLASSIFICADOR DE IDADE ===")
    try:
        idade = int(input("Digite sua idade: "))
        
        if idade < 0:
            print("Idade inválida! Digite um valor positivo.")
        elif idade <= 12:
            print(f"Você tem {idade} anos e é classificado como: Criança")
        elif idade <= 17:
            print(f"Você tem {idade} anos e é classificado como: Adolescente")
        elif idade <= 59:
            print(f"Você tem {idade} anos e é classificado como: Adulto")
        else:
            print(f"Você tem {idade} anos e é classificado como: Idoso")
    except ValueError:
        print("Por favor, digite um número válido!")

# 2 - CALCULADORA DE IMC
def calculadora_imc():
    print("\n=== CALCULADORA DE IMC ===")
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos!")
            return
        
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        
    except ValueError:
        print("Por favor, digite valores numéricos válidos!")

# 3 - CONVERSOR DE TEMPERATURA
def conversor_temperatura():
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    print("Unidades disponíveis: C (Celsius), F (Fahrenheit), K (Kelvin)")
    
    try:
        temperatura = float(input("Digite a temperatura: "))
        origem = input("Digite a unidade de origem (C/F/K): ").upper()
        destino = input("Digite a unidade de destino (C/F/K): ").upper()
        
        if origem not in ['C', 'F', 'K'] or destino not in ['C', 'F', 'K']:
            print("Unidades inválidas! Use C, F ou K.")
            return
        
        # Converter tudo para Celsius primeiro
        if origem == 'F':
            celsius = (temperatura - 32) * 5/9
        elif origem == 'K':
            celsius = temperatura - 273.15
        else:  # origem == 'C'
            celsius = temperatura
        
        # Converter de Celsius para a unidade de destino
        if destino == 'F':
            resultado = celsius * 9/5 + 32
        elif destino == 'K':
            resultado = celsius + 273.15
        else:  # destino == 'C'
            resultado = celsius
        
        print(f"{temperatura}°{origem} = {resultado:.2f}°{destino}")
        
    except ValueError:
        print("Por favor, digite uma temperatura válida!")

# 4 - VERIFICADOR DE ANO BISSEXTO
def verificador_ano_bissexto():
    print("\n=== VERIFICADOR DE ANO BISSEXTO ===")
    try:
        ano = int(input("Digite um ano: "))
        
        # Um ano é bissexto se:
        # - É divisível por 4 E
        # - NÃO é divisível por 100 OU é divisível por 400
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"O ano {ano} é bissexto!")
        else:
            print(f"O ano {ano} não é bissexto.")
            
    except ValueError:
        print("Por favor, digite um ano válido!")

# MENU PRINCIPAL
def menu_principal():
    while True:
        print("\n" + "="*40)
        print("ESCOLHA UM PROGRAMA:")
        print("1 - Classificador de Idade")
        print("2 - Calculadora de IMC")
        print("3 - Conversor de Temperatura")
        print("4 - Verificador de Ano Bissexto")
        print("5 - Sair")
        print("="*40)
        
        try:
            opcao = int(input("Digite sua opção (1-5): "))
            
            if opcao == 1:
                classificador_idade()
            elif opcao == 2:
                calculadora_imc()
            elif opcao == 3:
                conversor_temperatura()
            elif opcao == 4:
                verificador_ano_bissexto()
            elif opcao == 5:
                print("Obrigado por usar nossos programas!")
                break
            else:
                print("Opção inválida! Digite um número de 1 a 5.")
                
        except ValueError:
            print("Por favor, digite um número válido!")

# EXECUTAR O PROGRAMA
if __name__ == "__main__":
    menu_principal()