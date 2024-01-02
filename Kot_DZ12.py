# №1
# class CardDeck:
#     def __init__(self):
#         self.lenght = 52
#         self.index = 0
#         self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
#         self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index < self.lenght:
#             suit = self.__SUITS[self.index // len(self.__RANKS)]
#             rank = self.__RANKS[self.index % len(self.__RANKS)]
#             self.index += 1
#             return f'{rank} {suit}'
#         else:
#             raise StopIteration
#
# card = CardDeck()
# for i in card:
#     print(i)

# №2

def fib(num):
    num1, num2 = 0, 1
    for i in range(num):
        num1, num2 = num2, num1 + num2
        yield num1

print(list(fib(10)))
