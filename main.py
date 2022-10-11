from random import randint
import os

class MontyHall:
    __answer = None
    __chosen_door = None
    __doors = None

    def __init__(self, number_of_doors):
        self.__number_of_doors = number_of_doors

    def generate_answer(self):
        self.__doors = [False for i in range(self.__number_of_doors)]
        self.__doors[(randint(0, self.__number_of_doors - 1))] = True

    def choose_door(self, index):
        self.__chosen_door = index

    def open_all_doors_except_two(self):
        if self.__doors[self.__chosen_door - 1]:
            self.__doors = [False, True]
            self.__chosen_door = 1
        else:
            self.__doors = [False, True]
            self.__chosen_door = 0

    def swap_choose(self):
        if self.__chosen_door == 1:
            self.__chosen_door = 0
        else:
            self.__chosen_door = 1

    def open_doors(self):
        return self.__doors[self.__chosen_door]


def main():
    results = {"win": 0,
               "lose": 0}
    num_of_tests = int(input("Enter num of tests:\n>"))
    num_of_doors = int(input("Enter num of doors:\n>"))
    current_test = 0
    game = MontyHall(num_of_doors)
    while current_test != num_of_tests:
        game.generate_answer()
        game.choose_door(randint(1, num_of_doors))
        game.open_all_doors_except_two()
        game.swap_choose()
        answer = game.open_doors()
        if answer:
            results["win"] += 1
        else:
            results["lose"] += 1
        current_test += 1
        if current_test % 1000 == 0:
            print(f"Counting...\nCurrent num of processed tests: {current_test}")

    print(f"-----COMPLETED!-----\nProcessed tests: {num_of_tests}\nNumber of doors: {num_of_doors}\n"
          f"WINS with swapping the door: {results['win']}\n"
          f"LOSES with swapping the door: {results['lose']}\n"
          f"\nTOTAL WIN RATE: {results['win'] / num_of_tests * 100}%")
    input()


if __name__ == "__main__":
    main()