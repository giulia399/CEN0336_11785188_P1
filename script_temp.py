# script_temp.py

# Função para converter Celsius em Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (9/5) * celsius + 32

# Solicita ao usuário que insira uma lista de temperaturas em Celsius
entrada = input("Digite as temperaturas em graus Celsius (separadas por espaço): ")

# Tenta converter a entrada em uma lista de números
try:
    # Divide a entrada em uma lista e converte cada item para float
    temperaturas_celsius = [float(temp) for temp in entrada.split()]
except ValueError:
    print("Por favor, insira apenas números válidos.")
    exit()

# Inicializa uma lista vazia para armazenar as temperaturas convertidas
temperaturas_fahrenheit = []

# Loop para converter cada temperatura
for celsius in temperaturas_celsius:
    fahrenheit = celsius_para_fahrenheit(celsius)
    temperaturas_fahrenheit.append(fahrenheit)

# Exibe os resultados
print("Celsius   Fahrenheit")
for celsius, fahrenheit in zip(temperaturas_celsius, temperaturas_fahrenheit):
    print(f"{celsius:<10} {fahrenheit:.1f}")
