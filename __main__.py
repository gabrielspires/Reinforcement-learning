from sys import argv
from pprint import pp

from warehouse import Warehouse
from qlearning import Qlearning

if __name__ == "__main__":
    input_file = argv[1]
    alpha = float(argv[2])  # Taxa de aprendizado
    lambda_ = float(argv[3])  # Fator de desconto
    epsilon = float(argv[4])  # Fator de exploração da estratégia epsilon-greedy
    n = int(argv[5])  # Número de episódios de treinamento

    warehouse = Warehouse(input_file)
    qlearning = Qlearning(warehouse, alpha, lambda_, epsilon, n)
    # import time
    # start = time.time()

    # Debug
    # Printa o arquivo, os argumentos e os steps (pra ver se ta pegando certo)
    print("\nFile: ", input_file, "\tMax steps:", warehouse.max_steps)
    print(qlearning)

    # Printa a q-table no formato final da saída (pra visualizar)
    print("Q-Table:\n x, y, w   move   reward")
    qlearning.show_q_table()

    # Printa o mapa do galpão (pra visualizar)
    warehouse.show_map()

    # Printa o dicionário da q-table (pra visualizar)
    # pp(qlearning.q_table)

    # Programa

    # qlearning.learn()

    # end = time.time()
    # print("Time elapsed -", input_file.split("/")[-1] + ", " + str(end - start) + "s")

# Info:

# Formato da Q-Table:
# {'x': {'y': {'steps_left': {'move': reward}}}}
# Saída do TP:
# (x, y, steps_left), move, best_reward
