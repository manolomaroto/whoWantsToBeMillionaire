import random
import time

class Contestant:
    number = 1
    points = 0
    winner = False
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
    print('')
    print('First question')
    print('')
    # List to save how long takes to each contestants to respond
    how_long = []
    for contesn in contestants:
        time_start = time.time()
        response = input(f'{contesn.name}, what is the capital of France? ')
        time_end = time.time()
        if response == 'Paris':
            contesn.points += random.random()
            contesn.winner = True
            # Calculate how long takes to respond
            how_long.append(time_end - time_start)
            print(f'That is correct!!!')
        else:
            print(f'Oh no, {response} is not the correct response!')

    index_faster = how_long.index(min(how_long))
    for idx, contesn in enumerate(contestants):
        # Look for the winner
        if contesn.winner == True and idx == index_faster:
            next_round(contesn)

def next_round(contesn):
    print('')
    print(f'{contesn.name} you are in the next round!!')
    print('')
    question = input('Whats is the highest mountain in the world? ')
    if question == 'Everest':
        print('')
        print(f'{contesn.name} you are the best ever!!!')
        print('')
    else:
        print('')
        print('Oh, no. You lost 1 billion!!!')
        print('')


start()



