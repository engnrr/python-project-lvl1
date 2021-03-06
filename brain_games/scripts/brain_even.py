#!/usr/bin/env python
import random
import game_engine


game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def qa_generator():  # question and right answer generation
    value = random.randint(1, 100)

    if value % 2 == 0:  # chek number is even
        right_answer = 'yes'
    else:
        right_answer = 'no'

    question_text = value
    return question_text, right_answer


def main():
    game_engine.game_logic()  # start The game


if __name__ == '__main__':
    main()
