from utils import show_map, read_input_file
from sys import argv

if __name__ == "__main__":
    input_file = argv[1]
    alpha = argv[2]  # Taxa de aprendizado
    lambda_ = argv[3]  # Fator de desconto
    epsilon = argv[4]  # Fator de exploração da estratégia epsilon-greedy
    n = argv[5]  # Número de episódios de treinamento

    map_height, map_width, max_steps, map_ = read_input_file(input_file)

    # import time
    # start = time.time()

    # Debug
    print("\nFile: ", input_file, "Max steps:", max_steps)
    print("Alpha:", alpha, "Lambda:", lambda_, "Epsilon:", epsilon, "Episodes:", n, "\n")
    show_map(map_)

    # Programa

    # end = time.time()
    # print("Time elapsed -", input_file.split("/")[-1] + ", " + str(end - start) + "s")
