import re

psychobabble_pattern = r"\b(?:ich|mein|mir|mich|fühlen|denken)\b"

def match_psychobabble(user_input):
    return re.search(psychobabble_pattern, user_input)
