# Importando o módulo sys para capturar os argumentos da linha de comando
import sys

# Função para calcular o quadrado da hipotenusa
def calcular_hipotenusa(a, b):
    return a**2 + b**2

# Verificando se o número correto de argumentos foi fornecido
if len(sys.argv) != 3:
    print("Erro: Você deve fornecer exatamente dois inteiros positivos menores que 500.")
    sys.exit(1)

# Capturando os argumentos da linha de comando
arg_a = sys.argv[1]
arg_b = sys.argv[2]

# Verificando se os argumentos são dígitos e convertendo para inteiros
if not arg_a.isdigit() or not arg_b.isdigit():
    print("Erro: Ambos os argumentos devem ser inteiros positivos.")
    sys.exit(1)

# Convertendo os argumentos para inteiros
a = int(arg_a)
b = int(arg_b)

# Verificando se os valores estão dentro do intervalo permitido
if a <= 0 or a >= 500 or b <= 0 or b >= 500:
    print("Erro: Os números devem ser positivos e menores que 500.")
    sys.exit(1)

# Calculando o quadrado da hipotenusa
hipotenusa_quadrado = calcular_hipotenusa(a, b)

# Imprimindo o resultado
print(f"O quadrado da hipotenusa para o triângulo retângulo com lados a={a} e b={b}, é {hipotenusa_quadrado}.")
