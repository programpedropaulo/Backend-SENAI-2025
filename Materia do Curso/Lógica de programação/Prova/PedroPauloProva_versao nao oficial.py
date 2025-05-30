#De Pedro paulo
#Me de sugestoes do que melhorar por favor
import random

valor = True
print("\nOlá, me chamo Lino! Vamos começar nossa brincadeira\n")

nome = input("Gostaria de te conhecer, então por favor me diga seu nome: ")
print(f"Prazer em te conhecer, {nome}!\n")

print("Adivinhe o número se puder!\n")

while valor:
    numeroAleatorio = random.randint(0, 100)
    print("Número para teste", numeroAleatorio)
    contador = 0
    
    while contador < 10:  # Limite de 10 tentativas
        print(f"Tentativa: {contador + 1}")  # Exibe a tentativa atual
        try:
            numeroInserido = int(input("Insira um número: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        if numeroAleatorio == numeroInserido:
            print(f"Parabéns, você acertou! O número era {numeroAleatorio}.")
            break  # Sai do loop de tentativas
        elif numeroInserido < numeroAleatorio:
            print("Dica: Aumente o número mais um pouco!")
        else:
            print("Dica: Abaixe um pouco mais.")
        
        if contador == 8:  # Alerta para a última tentativa
            print("Essa é sua última tentativa!")
        
        contador += 1
    
    # Fim do jogo, pergunta se quer jogar de novo
    print("\nReinicializando o jogo...")
    opcao = int(input("Digite 1 para começar outro jogo ou 0 para sair: "))
    
    if opcao == 0:
        valor = False

print("Obrigado por jogar!")
