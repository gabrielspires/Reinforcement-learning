import random

from colorama import Back, Fore, Style


class Warehouse(object):
    def __init__(self, input_file):
        self.map_ = []
        with open(input_file) as input_:
            map_info = list(map(int, input_.readline().split()))

            self.map_height = map_info[0]
            self.map_width = map_info[1]
            self.max_steps = map_info[2]

            for line in input_:
                self.map_.append(list(line[0:-1]))

        self.map_height += 1
        self.map_width += 1

    def random_valid_position(self):
        # Retorna uma posição aleatória válida dentro do mapa
        # O AGV começa em lugares aleatórios no q-learning
        # O ponto de coleta não pode ser um ponto inicial
        # A posição aleatória é entre 1 e dimensão-2 pra ignorar as paredes externas
        while True:
            x = random.randint(1, self.map_height - 2)
            y = random.randint(1, self.map_width - 2)

            if self.map_[x][y] == "." or self.map_[x][y] == "#":
                return (x, y)

    def show_map(self):
        num_linha = 0
        num_coluna = 0
        print(3 * " ", end="")
        for _ in range(len(self.map_[0])):
            print("{:<2}".format(num_coluna), end=" ")
            num_coluna += 1
        print()
        for linha in self.map_:
            print("{:<2}".format(num_linha), end=" ")
            num_linha += 1
            for caractere in linha:
                if caractere == "*":
                    print(
                        Back.LIGHTWHITE_EX + Fore.BLACK + "{:<2}".format(caractere),
                        end=" ",
                    )
                    print(Style.RESET_ALL, end="")
                elif caractere == "#":
                    print(
                        Back.GREEN + Fore.BLACK + "{:<2}".format(caractere),
                        end=" ",
                    )
                    print(Style.RESET_ALL, end="")
                elif caractere == "$":
                    print(
                        Back.LIGHTCYAN_EX + Fore.BLACK + "{:<2}".format(caractere),
                        end=" ",
                    )
                    print(Style.RESET_ALL, end="")
                else:
                    print("{:<2}".format(caractere), end=" ")
            print()
