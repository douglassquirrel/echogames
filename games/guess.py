from game_random import nth_random
from util import compare, to_digits

def guess(session_id, conversation):
    line = conversation[-1]
    guess = to_digits(line)
    seed = to_digits(session_id)
    target = nth_random(seed, 1, 100, 1)
    turns = len(conversation)//2 + 1

    results = {-1:"too low", 0:f"CORRECT in {turns} turns", 1:"too high"}
    result = results[compare(guess, target)]

    return f"Guess a number 1-100. Your guess of {guess} is {result}!"
