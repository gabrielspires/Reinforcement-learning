from sys import argv
from pprint import pp

from warehouse import Warehouse
from qlearning import Qlearning

if __name__ == "__main__":
    input_file = argv[1]
    alpha = float(argv[2])  # Taxa de aprendizado
    lambda_ = float(argv[3])  # Fator de desconto (que é gama na verdade)
    epsilon = float(argv[4])  # Fator de exploração da estratégia epsilon-greedy
    n = int(argv[5])  # Número de episódios de treinamento

    warehouse = Warehouse(input_file)
    qlearning = Qlearning(warehouse, alpha, lambda_, epsilon, n)
    # import time
    # start = time.time()

    # Debug
    # Printa o arquivo, os argumentos e os steps (pra ver se ta pegando certo)
    # print("\nFile: ", input_file, "\tMax steps:", warehouse.max_steps)
    # print(qlearning)

    # Printa a q-table no formato final da saída (pra visualizar)
    # print("Q-Table:\n x, y, w   move   reward")
    # qlearning.show_q_table()

    # Printa o mapa do galpão (pra visualizar)
    warehouse.show_map()

    # Printa o dicionário da q-table (pra visualizar)
    # pp(qlearning.q_table)

    # Programa

    qlearning.learn()

    # print("Q-Table:\n x, y, w   move   reward")
    qlearning.show_q_table()
    # end = time.time()
    # print("Time elapsed -", input_file.split("/")[-1] + ", " + str(end - start) + "s")

    with open(
        "rewards/"
        + argv[1]
        + "_"
        + str(alpha)
        + "_"
        + str(lambda_)
        + "_"
        + str(epsilon)
        + "_"
        + str(n)
        + ".txt",
        "w",
    ) as reward_mean_file:
        reward_mean_file.write(qlearning.show_mean_reward())

# Info:

# Modelagem MDP<S,A,R,T>
#   S = posições onde o AGV pode andar (*,., #, $)
#   A = conjunto de ações (RIGHT, LEFT, UP, DOWN) ver qlearning.moves
#   R = Função de recompensa (ver qlearning.reward())
#   T = Função de transição (UP no estado (3,1) leva para o estado (2,1) por exemplo),
#       se o AGV tentar se mover para uma parede ele continua no mesmo estado e ganha -10
#       ver qlearning.move()

# Formato da Q-Table:
# {'x': {'y': {'steps_left': {'move': reward}}}}
# Saída no formato do TP:
# (x, y, steps_left), move, best_reward

# duvidas
# as paredes tem que ter valor na qtable?