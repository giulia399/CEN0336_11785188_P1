# script_CDS.py

import sys

# Função para verificar se todos os números são inteiros e dentro do limite
def validar_argumentos(args):
    if len(args) != 7:
        print("Erro: São necessários exatamente 7 argumentos.")
        sys.exit(1)

    # Verifica se o primeiro argumento é uma string
    sequencia_dna = args[1]
    if not isinstance(sequencia_dna, str):
        print("Erro: A sequência de DNA deve ser uma string.")
        sys.exit(1)

    # Verifica se os demais argumentos são inteiros e válidos
    for i in range(2, 7):
        if not args[i].isdigit():
            print(f"Erro: O argumento {i} deve ser um número inteiro.")
            sys.exit(1)
        valor = int(args[i])
        if valor > len(sequencia_dna):
            print(f"Erro: O argumento {i} não pode ser maior que o comprimento da sequência de DNA.")
            sys.exit(1)

# Função principal
def main():
    # Valida os argumentos da linha de comando
    validar_argumentos(sys.argv)

    # Armazena os argumentos em variáveis
    sequencia_dna = sys.argv[1]
    n1, n2, n3, n4, n5, n6 = map(int, sys.argv[2:])

    # Extrai as sequências entre CDS
    sequencia_cds1_cds2 = sequencia_dna[n1:n2]
    sequencia_cds2_cds3 = sequencia_dna[n3:n4]

    # Verifica as condições para a sequência entre CDS 1 e CDS 2
    if sequencia_cds1_cds2.startswith("GT") and sequencia_cds1_cds2.endswith("AG"):
        print("A sequência entre CDS 1 e CDS 2 é válida.")
    else:
        print("A sequência entre CDS 1 e CDS 2 é inválida.")
        return

    # Verifica as condições para a sequência entre CDS 2 e CDS 3
    if sequencia_cds2_cds3.startswith("GT") and sequencia_cds2_cds3.endswith("AG"):
        print("A sequência entre CDS 2 e CDS 3 é válida.")
    else:
        print("A sequência entre CDS 2 e CDS 3 é inválida.")
        return

    # Se ambas as sequências são válidas, imprime a concatenação das CDS
    sequencia_resultante = sequencia_dna[n1:n2] + sequencia_dna[n3:n4] + sequencia_dna[n5:n6]
    print("Sequência resultante:", sequencia_resultante)

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
