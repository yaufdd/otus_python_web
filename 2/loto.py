import random
import numpy as np

class Player():
    
    def __init__(self, card, bingo):
        self._card = card  
        self.bingo = bingo

    def check_out(self, number, rows, cols):
        is_number_found = False
        for i in range(rows):
            for j in range(cols):
                if self._card[i][j] == number:
                    is_number_found = True
                    self._card[i][j] = "-"
        return is_number_found


class Card():
    
    def __init__(self, array, rows, cols, empty_cells_per_row, type):
        self.digits = array
        self.rows = rows
        self.cols = cols
        self.type = type
        self.empty_cells_per_row = empty_cells_per_row

        self._card = None
        self.set_card()

    def set_card(self):
        unique_numbers = list(range(1, 91))
        selected_numbers = random.sample(unique_numbers, 27)
        random.shuffle(selected_numbers)
        self.digits = [selected_numbers[i:i+self.cols] for i in range(0, self.cols * self.rows, self.cols)]
        for row in self.digits:
            empty_positions = random.sample(range(self.cols), self.empty_cells_per_row)
            for pos in empty_positions:
                row[pos] = None

        self._card = self.digits
    
    def get_card(self):
        return self._card
    
    def display_card(self):
        if self.type == "player":
            print("------- Карточка живого игрока ------")
            for row in self._card:
                row_str = '  '.join(['{:>2}'.format(item) if item is not None else '  ' for item in row])
                print(row_str)
            print("-------------------------------------")
        elif self.type == "pc":
            print("-------- Карточка компьютера --------")
            for row in self._card:
                row_str = '  '.join(['{:>2}'.format(item) if item is not None else '  ' for item in row])
                print(row_str)
            print("-------------------------------------")
        

class Meshok():
    def __init__(self, amount):
        self._amount = amount
        self._numbers = None

        self.set_numbers()

    def get_amount(self):
        return self._amount

    def set_numbers(self):
        ls = list(range(1, 91))
        random.shuffle(ls)
        self.numbers = ls
        

    def get_numbers(self):
        return self.numbers

    def get_new_bochonok(self):
        self._amount -= 1
        new_bochonok = self.numbers[self._amount]
        
        return new_bochonok
    

class Game():
    def __init__(self):
        self.game_status = None

    def start(self):
        self.game_status = True

    def end(self):
        self.game_status = False

    def is_choice_right(self, result):
        choice = input("Зачеркнуть цифру? (y/n)")
        if choice == "y" and result == False:
            print("Цифры на самом деле нет.Игра завершена")
            self.game_status = False
        elif choice == "n" and result == True:
            print("Цифрa на самом деле есть.Игра завершена")
            self.game_status = False

    
class GameSetting():
    def __init__(self, players_list):
        self._player_amount = None
        self.players_list = players_list

    def set_player_amount(self):
        player_amount = int(input("Сколько игроков будет играть?: "))
        self._player_amount = player_amount

    def get_player_amount(self):
        return self._player_amount
    
    def set_players_list(self):
        for i in range(self._player_amount):
            player_type = input(f"Игрок{i + 1}  человек или компьютер? (player/pc)")
            card = Card(array, 3, 9, 4, player_type)
            player = Player(card.get_card(), 0)
            self.players_list.append({player : card})

    def get_players_list(self):
        return self.players_list
        


array = []
players_list = []

game = Game()
meshok = Meshok(90)
game_setting = GameSetting(players_list)

game_setting.set_player_amount()
player_amount = game_setting.get_player_amount()
game_setting.set_players_list()
players_list = game_setting.get_players_list()

game.start()
while(game.game_status):
    curent_bochonok = meshok.get_new_bochonok()
    print(f"Новый бочонок: {curent_bochonok} (осталось {meshok.get_amount()})")

    for player in players_list:
        pl, card = next(iter(player.items()))

        if pl.bingo == 15:
            game.end()

        card.display_card()

        if card.type == "player":
            is_in_player_card = pl.check_out(curent_bochonok, card.rows, card.cols)
            pl.bingo += 1

            game.is_choice_right(is_in_player_card)

        elif card.type == "pc":
            is_in_player_card = pl.check_out(curent_bochonok, card.rows, card.cols)
            if is_in_player_card:
                pl.check_out(curent_bochonok, card.rows, card.cols)
                pl.bingo += 1

    print("\n")

print("Спасибо за игру")

    
        


            