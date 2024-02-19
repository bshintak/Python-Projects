def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero."

def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))

            if operacao == "+":
                resultado = adicao(num1, num2)
            elif operacao == "-":
                resultado = subtracao(num1, num2)
            elif operacao == "*":
                resultado = multiplicacao(num1, num2)
            elif operacao == "/":
                resultado = divisao(num1, num2)
            else:
                print("Operação inválida. Tente novamente.")
                continue

            print(f"Resultado: {resultado}")

            continuar = input("Deseja fazer outra operação? (s/n): ")
            if continuar.lower() != 's':
                print("Calculadora encerrada. Até mais!")
                break

        except ValueError:
            print("Por favor, insira números válidos.")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    calculadora()
