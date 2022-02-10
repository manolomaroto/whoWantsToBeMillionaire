class Contestant:
    number = 1
    def __init__(self, name):
        self.name = name
        self.number = Contestant.number
        Contestant.number += 1
    
    def __repr__(self):
        return f'Contest name is {self.name} with number {self.number}'

def start():
    print('***********************************************************')
    print('')
    print('        WELCOME TO WHO WANTS TO BE MILLIONAIRE!!!!!         ')
    print('')
    print('***********************************************************')
    print('')
    print('')

    contestants = 0
    contestants = input('How many contestants are there? ')
    print('')
    print('There are ' + contestants + ' contestants.')

    create_contestants(contestants)

def create_contestants(number_contestants):
    for i in range(0, int(number_contestants)):
        name = input('Insert name contestant ' + str(i + 1) + ': ')
        globals()[f'contestant{i + 1}']= Contestant(name)


start()

print(contestant1.__repr__())
print(contestant2.__repr__())

