import random

class Contestant:
    number = 1
    points = 0
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

    instances = create_contestants(contestants)

    first_question(instances)

def create_contestants(number_contestants):
    total_constestants = []
    for i in range(0, int(number_contestants)):
        name = input('Insert name contestant ' + str(i + 1) + ': ')
        """ globals()[f'contestant{i + 1}']= Contestant(name)
        total_constestants.append('contestant' + str(i + 1)) """
        total_constestants.append(Contestant(name))
    return total_constestants

def first_question(contestants):
    for contesn in contestants:
        response = input('What is the capital of France? ')
        if response == 'Paris':
            contesn.points += random.random()
            print(f'You have won {contesn.points} points')
        else:
            print(f'Oh no, {response} is not the correct response!')




start()



