import random

opcoes = {1: 'Pedra', 2: 'Papel', 3: 'Tesoura', 4: 'Lagarto', 5: 'Spock'}

vitorias = {1: [3, 4], 2: [1, 5], 3: [2, 4], 4: [5, 2], 5: [3, 1]}

while True:
    try:
        player_input = input('Selecione uma opção: \n1 - Pedra\n2 - Papel\n3 - Tesoura\n4 - Lagarto\n5 - Spock\n(Ou digite "Sair" para encerrar o jogo)\n')

        if player_input.lower() == 'sair':
            print("Jogo encerrado. Até mais!")
            break

        player = int(player_input)

        if player not in opcoes:
            print("Opção inválida. Por favor, escolha um número de 1 a 5 ou digite 'Sair'.")
            continue

        computer = random.randint(1, 5)

        print(f"Você escolheu {opcoes[player]} e o computador {opcoes[computer]}.")

        if player == computer:
            print('Empate!')
        elif computer in vitorias[player]:
            print('Você ganhou!')
        else:
            print('Você perdeu!')

        print("-" * 45)

    except ValueError:
        print('Entrada inválida. Por favor, digite um número (1 a 5) ou "Sair".')
    except KeyError:
        print("Erro inesperado com a opção. Tente novamente.")