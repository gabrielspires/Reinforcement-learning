from sys import argv

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
    print("\nFile: ", input_file, "\tMax steps:", warehouse.max_steps)
    print(qlearning)
    # print("Posição inicial:", warehouse.random_valid_position())
    print("Q-Table:\n x, y, w   move   reward")
    qlearning.show_q_table()
    warehouse.show_map()

    # Programa

    # end = time.time()
    # print("Time elapsed -", input_file.split("/")[-1] + ", " + str(end - start) + "s")
