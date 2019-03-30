from string import ascii_uppercase
from random import choice, randint
from numpy.random import choice as weighted_choice
from ipdb import set_trace


class Characters(object):

    def __init__(self, characters=None):

        if characters is None:

            self.characters = [choice(ascii_uppercase) for index in range(18)]

        else:

            self.characters = characters

    def calculate_fitness(self, expected_characters):

        matching_characters = 0

        for self_character, expected_character in (
            zip(self.characters, expected_characters)
        ):

            if self_character == expected_character:

                matching_characters = matching_characters + 1

            if matching_characters == len(expected_characters):

                raise Exception('Found!')

        return matching_characters / len(expected_characters)

    def mutate(self):

        if randint(0, 99) == 50:

            print('Mutated!')

            self.characters[randint(0, len(self.characters) - 1)] = choice(
                ascii_uppercase
            )

    def __repr__(self):

        return ''.join(self.characters)


def reproduce(first_characters, second_characters):

    child_characters = []

    for first_character, second_character in zip(
        first_characters.characters, second_characters.characters
    ):

        if randint(0, 1):

            child_characters.append(first_character)

        else:

            child_characters.append(second_character)

    return Characters(child_characters)


population = [Characters() for index in range(1000)]

expected_characters = 'ABCDEFGHIJKLMNOPQR'

population_counter = 1

while True:

    for characters in population:

        print(characters)

    print()
    print(population_counter)
    print()

    population_counter = population_counter + 1

    probabilities = [
        characters.calculate_fitness(expected_characters)
        for characters in population
    ]

    probability_sum = sum(probabilities)

    set_trace

    probabilities = [
        probability / probability_sum for probability in probabilities
    ]

    new_population = []

    for characters in population:

        child = reproduce(
            weighted_choice(population, p=probabilities),
            weighted_choice(population, p=probabilities)
        )

        child.mutate()

        new_population.append(child)

    population = new_population
