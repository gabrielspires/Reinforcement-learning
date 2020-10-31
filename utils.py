from colorama import Back, Fore, Style


def read_input_file(input_file):
    map_ = []
    with open(input_file) as input_:
        map_height, map_width, max_steps = list(map(int, input_.readline().split()))
        for line in input_:
            map_.append(list(line[0:-1]))

    return map_height + 1, map_width + 1, max_steps, map_


def show_map(mapa):
    num_linha = 0
    num_coluna = 0
    print(3 * " ", end="")
    for _ in range(len(mapa[0])):
        print("{:<2}".format(num_coluna), end=" ")
        num_coluna += 1
    print()
    for linha in mapa:
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
