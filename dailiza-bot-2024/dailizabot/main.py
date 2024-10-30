import random
import re
from dailizabot.reflection import reflect
from dailizabot.text_patterns import psychobabble


def dailiza_answer(user_input):
    """Generation of answers for DAILIZA-like bot.

    Parameters
    ----------
    user_input
        String with user input for DAILIZA to respond to.
    """

    # Test input string for all known text patter in pychobabble
    for pattern, responses in psychobabble:
        match = re.search(pattern.lower(), str(user_input).lower().strip())
        if match:
            rspns = random.choice(responses)
            return rspns.format(*[reflect(g) for g in match.groups()])
    return "Das habe ich nicht verstanden. Bitte wiederhole es!"


def run_dailiza_bot():
    """Starts the DAILIZA bot.
    """
    print("Hey Hallo! Ich bin Dailiza. Womit kann ich dir helfen?")
    user_input = ""
    while "exit" not in user_input:
        user_input = input(">> ")
        print(dailiza_answer(user_input))


if __name__ == '__main__':
    run_dailiza_bot()