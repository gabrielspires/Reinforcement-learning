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
                # for steps_left in range(0, self.steps_left + 1):
                #     self.q_table[str(i)][str(j)][str(steps_left)] = {}
                for move in self.moves:
                    self.q_table[str(i)][str(j)].update({move: 0.0})

    def show_q_table(self):

        q_table_size = 0
        q_table = ""
        for x in self.q_table:
            for y in self.q_table[x]:
                # for steps_left in self.q_table[x][y]:
                for move in self.q_table[x][y]:
                    if self.warehouse.map_[int(x)][int(y)] != "*":
                        q_table_size += 1
                        q_table += f"({x}, {y}, {0000}), {move},"
                        q_table += f'{"%0.2f" % self.q_table[x][y][move]}\n'
        print(q_table)
        print("Q-Table size:", q_table_size)

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

        # Se o estado for "." a recompensa é -1
        if self.warehouse.map_[i][j] == ".":
            reward = -1
        # Se o estado for "#" a recompensa é +1
        elif self.warehouse.map_[i][j] == "#":
            reward = 1
        # Se o estado for "$" a recompensa é +10
        elif self.warehouse.map_[i][j] == "$":
            reward = 10
        # Se o estado for "*" a recompensa é -10
        # Se o número de passos restantes é 0 a recompensa é -10
        elif self.warehouse.map_[i][j] == "*":  # or self.steps_left - 1 <= 0:
            reward = -10

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

        # Evita erros quando o estado fica onde era pra ser a parede externa
        if new_x < 0 or new_x > self.warehouse.map_height - 1:
            return
        if new_y < 0 or new_y > self.warehouse.map_width - 1:
            return

        steps_left_before = self.steps_left
        self.steps_left -= 1

        # if self.steps_left <= 0:
        #     return

        # Encontra um ponto de localização e reseta o número de passos
        if self.warehouse.map_[new_x][new_y] == "#":
            self.steps_left = self.warehouse.max_steps

        # if self.warehouse.map_[new_x][new_y] == "*":
        #     new_x = self.actual_state[0]
        #     new_y = self.actual_state[1]

        new_x = str(new_x)
        new_y = str(new_y)

        old_x = str(self.actual_state[0])
        old_y = str(self.actual_state[1])

        max_new_state = self.q_table[new_x][new_y][  # [str(self.steps_left)][
            max(
                self.q_table[new_x][new_y],  # [str(self.steps_left)],
                key=self.q_table[new_x][new_y].get,  # [str(self.steps_left)].get,
            )
        ]

        self.q_table[old_x][old_y][direction] += self.alpha * (  # [str(steps_left_before)][
            self.reward(new_x, new_y)
            + self.lambda_ * max_new_state
            - self.q_table[old_x][old_y][direction]  # [str(steps_left_before)][
        )

        self.actual_state = (int(new_x), int(new_y))
        new_state = self.warehouse.map_[self.actual_state[0]][self.actual_state[1]]

        if new_state == "*" or new_state == "$":  # or self.steps_left <= 0:
            # Fim do episodio
            self.actual_state = self.warehouse.random_valid_position()
            self.steps_left = self.warehouse.max_steps

            self.n -= 1

            mean_reward = 0
            num_rewards = 0
            for x in self.q_table:
                for y in self.q_table[x]:
                    position = self.warehouse.map_[int(x)][int(y)]
                    if position != "." and position != "#":
                        continue
                    for action in self.q_table[x][y]:  # [str(self.steps_left)]:
                        mean_reward += self.q_table[x][y][action]  # [str(self.steps_left)]
                        num_rewards += 1

            mean_reward /= num_rewards
            self.mean_reward.append([self.episode, mean_reward])
            self.episode += 1

    def show_mean_reward(self):
        values = ""
        for episode in self.mean_reward:
            values += str(episode[0]) + " " + str(episode[1]) + "\n"
        return values

    def learn(self):
        while self.n:
            # if self.steps_left <= 0:
            #     self.steps_left = self.warehouse.max_steps
            if random.uniform(0, 1) < self.epsilon:
                # Exploration
                self.move(random.choice(self.moves))
            else:
                # Exploitation
                x = str(self.actual_state[0])
                y = str(self.actual_state[1])
                # from pprint import pp

                # pp(self.q_table)
                # print(self.q_table[x][y][str(self.steps_left)].get)
                # print(x, y)
                best_move = max(
                    self.q_table[x][y],  # [str(self.steps_left)],
                    key=self.q_table[x][y].get,  # [str(self.steps_left)].get,
                )
                self.move(best_move)
