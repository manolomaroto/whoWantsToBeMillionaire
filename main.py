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

class Contestant:
    number = 1
    def __init__(self, name):
        self.name = name
        self.number = Contestant.number
        Contestant.number += 1
    
    def __repr__(self):
        return f'Contest name is {self.name} with number {self.number}'

for i in range(0, int(contestants)):
    name = input('Insert name contestant ' + str(i + 1) + ': ')
    globals()[f'contestant{i}']= Contestant(name)

print(contestant0.__repr__())
print(contestant1.__repr__())

