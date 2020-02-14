from itertools import cycle


class User:
    def __init__(self, symbol):
        self.name = input(f'Введите имя игрока играющего {symbol}\n')
        self.symbol = symbol
        self.__win = 0
        self.__los = 0


class Board:

    def __init__(self, size=3):
        size = abs(size)
        if not size % 2 or size < 3:
            size += 1
        self.__board = [['_' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        board_str = ''
        for line in self.__board:
            board_str += '|'.join(line) + '\n'
        print(board_str)

    def add_symbol(self, symbol, x: int, y: int):
        self.__board[x - 1][y - 1] = symbol

    def check_cell(self, x, y):
        try:
            cell = self.__board[x - 1][y - 1]
            if cell == '_':
                return True
        except IndexError:
            return False
        return False

    def len_board(self):
        return len(self.__board)

    def check_win(self):
        # todo тут не самый оптимальный код, почему? сделайте лучше

        lines = []
        lines.extend(self.__board)  # добавляем горизонтали
        lines.extend(list(zip(*self.__board)))  # добавляем вертикали (поворачивая матрицу)
        lines.append([value[idx] for idx, value in enumerate(self.__board)])  # добавляем диаональ
        lines.append([value[idx] for idx, value in enumerate(zip(*self.__board[::-1]))])  # добавляем диаональ
        for line in lines:
            tmp = list(set(line))
            if len(tmp) == 1 and not tmp[0] == '_':
                return True, tmp[0]
        return False, '_'


class Game:
    def __init__(self):
        self.users = []
        self.__board = Board()
        self.__step = 0
        self.game_number = 0

    def __create_user(self):
        self.users = [User(symbol) for symbol in 'XO']

    def start_game(self):
        self.game_number += 1
        if not self.users:
            self.__create_user()

        for user in cycle(self.users):
            # todo Игра завершается без вывода статистики, и без реванша
            self.__step += 1
            self.__board.print_board()
            print(f'{"*" * 5} {user.name} {"*" * 5}')
            coordinates = self.__get_user_step()
            self.__board.add_symbol(user.symbol, *coordinates)
            win = self.__board.check_win()
            if win[0]:
                print(f'Победил игрок: {user.name}')
                break
            if self.__board.len_board() ** 2 <= self.__step:
                print('Победила Дружба')
                break
        print('*'*10)
        print('Игра окончена')

    def __get_user_step(self) -> tuple:
        while True:
            response = input('Введите координаты вашего хода через пробел\n')
            try:
                x, y = map(int, response.split())
                if not self.__board.check_cell(x, y):
                    raise ValueError
            except ValueError:
                print('Ошибка ввода повторите')
                continue
            return x, y


if __name__ == '__main__':
    game = Game()
    game.start_game()
