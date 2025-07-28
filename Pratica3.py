# ============================================================================
# EXERCÍCIO 1: CALCULADORA COM TRATAMENTO DE ERROS
# ============================================================================

def calculadora():
    """
    Calculadora que realiza as quatro operações básicas com tratamento de erros.
    """
    print("=== CALCULADORA ===")
    print("Operações disponíveis: + - * /")
    
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro: Por favor, digite um número válido!")
    
    while True:
        try:
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Erro: Por favor, digite um número válido!")
    
    while True:
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        
        try:
            if operacao == '+':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
                break
            elif operacao == '-':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
                break
            elif operacao == '*':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
                break
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida!")
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
                break
            else:
                print("Erro: Operação inválida! Use apenas +, -, * ou /")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")
            # Solicita novo segundo número
            while True:
                try:
                    num2 = float(input("Digite um novo segundo número (diferente de zero): "))
                    break
                except ValueError:
                    print("Erro: Por favor, digite um número válido!")


# ============================================================================
# EXERCÍCIO 2: REGISTRO DE NOTAS
# ============================================================================

def registro_notas():
    """
    Programa para registrar notas de uma turma e calcular a média.
    """
    print("\n=== REGISTRO DE NOTAS ===")
    print("Digite as notas (0 a 10) ou 'fim' para encerrar")
    
    notas = []
    
    while True:
        entrada = input("Digite uma nota: ").strip().lower()
        
        if entrada == 'fim':
            break
            
        try:
            nota = float(entrada)
            
            # Verifica se a nota está no intervalo válido
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f"Nota {nota} registrada com sucesso!")
            else:
                print("Erro: A nota deve estar entre 0 e 10!")
                
        except ValueError:
            print("Erro: Digite um número válido ou 'fim' para encerrar!")
    
    # Calcula e exibe a média
    if notas:
        media = sum(notas) / len(notas)
        print(f"\nTotal de notas registradas: {len(notas)}")
        print(f"Notas: {notas}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota foi registrada.")


# ============================================================================
# EXERCÍCIO 3: VERIFICADOR DE SENHA FORTE
# ============================================================================

def verificador_senha():
    """
    Programa que verifica se uma senha é forte.
    Critérios: pelo menos 8 caracteres e pelo menos um número.
    """
    print("\n=== VERIFICADOR DE SENHA ===")
    print("Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número")
    print("Digite 'sair' para encerrar")
    
    while True:
        senha = input("Digite sua senha: ")
        
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break
            
        # Verifica se a senha tem pelo menos 8 caracteres
        if len(senha) < 8:
            print("Erro: A senha deve ter pelo menos 8 caracteres!")
            continue
            
        # Verifica se a senha contém pelo menos um número
        tem_numero = any(char.isdigit() for char in senha)
        
        if not tem_numero:
            print("Erro: A senha deve conter pelo menos um número!")
            continue
            
        # Se chegou até aqui, a senha é forte
        print("Parabéns! Sua senha é forte!")
        break


# ============================================================================
# EXERCÍCIO 4: CONTADOR DE PARES E ÍMPARES
# ============================================================================

def contador_pares_impares():
    """
    Programa que solicita números inteiros e conta quantos são pares e ímpares.
    """
    print("\n=== CONTADOR DE PARES E ÍMPARES ===")
    print("Digite números inteiros ou 'fim' para encerrar")
    
    pares = 0
    impares = 0
    numeros_inseridos = []
    
    while True:
        entrada = input("Digite um número inteiro: ").strip().lower()
        
        if entrada == 'fim':
            break
            
        try:
            numero = int(entrada)
            numeros_inseridos.append(numero)
            
            if numero % 2 == 0:
                print(f"{numero} é PAR")
                pares += 1
            else:
                print(f"{numero} é ÍMPAR")
                impares += 1
                
        except ValueError:
            print("Erro: Digite um número inteiro válido ou 'fim' para encerrar!")
    
    # Exibe o resultado final
    print(f"\n=== RESULTADO FINAL ===")
    print(f"Números inseridos: {numeros_inseridos}")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")
    print(f"Total de números válidos: {pares + impares}")


# ============================================================================
# MENU PRINCIPAL
# ============================================================================

def menu_principal():
    """
    Menu principal para escolher qual exercício executar.
    """
    while True:
        print("\n" + "="*50)
        print("MENU PRINCIPAL - EXERCÍCIOS PYTHON")
        print("="*50)
        print("1. Calculadora")
        print("2. Registro de Notas")
        print("3. Verificador de Senha")
        print("4. Contador de Pares e Ímpares")
        print("5. Sair")
        print("="*50)
        
        try:
            opcao = int(input("Escolha uma opção (1-5): "))
            
            if opcao == 1:
                calculadora()
            elif opcao == 2:
                registro_notas()
            elif opcao == 3:
                verificador_senha()
            elif opcao == 4:
                contador_pares_impares()
            elif opcao == 5:
                print("Programa encerrado. Obrigado!")
                break
            else:
                print("Opção inválida! Escolha entre 1 e 5.")
                
        except ValueError:
            print("Erro: Digite um número válido!")


# ============================================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================================

if __name__ == "__main__":
    menu_principal()