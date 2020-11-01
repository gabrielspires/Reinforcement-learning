from sys import argv

from warehouse import Warehouse

if __name__ == "__main__":
    input_file = argv[1]
    alpha = argv[2]  # Taxa de aprendizado
    lambda_ = argv[3]  # Fator de desconto
    epsilon = argv[4]  # Fator de exploração da estratégia epsilon-greedy
    n = argv[5]  # Número de episódios de treinamento

    warehouse = Warehouse(input_file)

    # import time
    # start = time.time()

    # Debug
    print("\nFile: ", input_file, "\tMax steps:", warehouse.max_steps)
    print("Alpha:", alpha, "Lambda:", lambda_, "Epsilon:", epsilon, "Episodes:", n, "\n")
    print("Posição inicial:", warehouse.random_valid_position())
    warehouse.show_map()

    # Programa

    # end = time.time()
    # print("Time elapsed -", input_file.split("/")[-1] + ", " + str(end - start) + "s")
