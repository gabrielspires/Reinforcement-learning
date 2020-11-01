import random


class Qlearning(object):
    def __init__(self, warehouse, alpha, lambda_, epsilon, n):
        self.warehouse = warehouse
        self.alpha = alpha
        self.lambda_ = lambda_
        self.epsilon = epsilon
        self.n = n
        self.steps_left = warehouse.max_steps
        self.actual_state = warehouse.random_valid_position()
        self.moves = ["RIGHT", "LEFT", "UP", "DOWN"]

        self.mean_reward = []
        self.episode = 0

        # Criação da Q-table
        self.q_table = {}
        for i in range(len(self.warehouse.map_)):
            self.q_table[str(i)] = {}
            for j in range(len(self.warehouse.map_[i])):
                self.q_table[str(i)][str(j)] = {}
                for steps_left in range(0, self.steps_left + 1):
                    self.q_table[str(i)][str(j)][str(steps_left)] = {}
                    position = self.warehouse.map_[i][j]
                    if position == "." or position == "#":
                        for move in self.moves:
                            self.q_table[str(i)][str(j)][str(steps_left)].update({move: 0.0})

    def show_q_table(self):

        q_table_size = 0
        q_table = ""
        for x in self.q_table:
            for y in self.q_table[x]:
                for steps_left in self.q_table[x][y]:
                    for move in self.q_table[x][y][steps_left]:
                        position = self.warehouse.map_[int(x)][int(y)]
                        if position == "." or position == "#":
                            q_table_size += 1
                            q_table += f"({x}, {y}, {steps_left}), {move},"
                            q_table += f'{"%0.2f" % self.q_table[x][y][steps_left][move]}\n'
        print(q_table)
        print("Q-Table size:", q_table_size)
        # Q-Table:
        #  x, y, w   move   reward
        # (1, 1, 0), RIGHT, 0.00
        # (1, 1, 0), LEFT,  0.00
        # (1, 1, 0), UP,    0.00
        # (1, 1, 0), DOWN,  0.00
        # (1, 1, 1), RIGHT, 0.00
        # (1, 1, 1), LEFT,  0.00
        # (1, 1, 1), UP,    0.00
        # (1, 1, 1), DOWN,  0.00
        # ...

    def __str__(self):
        return (
            "Alpha: "
            + str(self.alpha)
            + " Lambda: "
            + str(self.lambda_)
            + " Epsilon: "
            + str(self.epsilon)
            + " Episodes: "
            + str(self.n)
            + "\n"
        )

    def reward(self, i, j):
        i = int(i)
        j = int(j)
        reward = 0

        # Se o número de passos restantes é 0 e o estado não é "#" a recompensa é -10
        if self.warehouse.map_[i][j] != "#" and self.steps_left == 0:
            reward = -10
        # Se o estado for "." a recompensa é -1
        elif self.warehouse.map_[i][j] == ".":
            reward = -1
        # Se o estado for "#" a recompensa é +1
        elif self.warehouse.map_[i][j] == "#":
            reward = 1
            # Atualizar self.steps_left aqui ????????????????????????????
        # Se o estado for "*" a recompensa é -10
        elif self.warehouse.map_[i][j] == "*":
            reward = -10
        # Se o estado for "$" a recompensa é +10
        elif self.warehouse.map_[i][j] == "$":
            reward = 10

        return reward

    def move(self, direction):
        if direction == "RIGHT":
            new_x = self.actual_state[0]
            new_y = self.actual_state[1] + 1
        elif direction == "LEFT":
            new_x = self.actual_state[0]
            new_y = self.actual_state[1] - 1
        elif direction == "UP":
            new_x = self.actual_state[0] - 1
            new_y = self.actual_state[1]
        elif direction == "DOWN":
            new_x = self.actual_state[0] + 1
            new_y = self.actual_state[1]

        # Bate na parede
        if self.maze.maze[new_x][new_y] == "*":
            new_x = self.actual_state[0]
            new_y = self.actual_state[1]

        new_x = str(new_x)
        new_y = str(new_y)

        old_x = str(self.actual_state[0])
        old_y = str(self.actual_state[1])