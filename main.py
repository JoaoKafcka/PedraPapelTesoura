import random

opcoes = {1: 'pedra',2: 'papel',3: 'tesoura'}

while True:
    try:
        player_input = input('Selecione uma opção: \n1 - pedra\n2 - papel\n3 - tesoura\n ')
        player = int(player_input)
        if player in opcoes:
            break
        else:
            print("Opção invalida. Por favor, escolha 1, 2 ou 3.")
    except ValueError:
        print('Entrada inválida. Por favor, digite um número (1, 2 ou 3).')

computer = random.randint(1, 3)

print(f"Você escolheu {opcoes[player]} e o computador {opcoes[computer]}.")

if player - computer == 1 or player - computer == -2:
    print('Você ganhou!')
elif player - computer == -1 or player - computer == 2:
    print('Você perdeu!')
elif player - computer == 0:
    print('Empate')
