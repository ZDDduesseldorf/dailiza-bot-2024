import re

def psychobabble(input_text):
    # Regex-Muster für verschiedene Fragen und Aussagen
    patterns = {
        r'\b(hast du)\b': "Was möchtest du wissen?",
        r'\b(ich\s+will)\b': "Warum möchtest du das?",
        r'\b(du\s+bist)\b': "Was denkst du über das?",
    }

    for pattern, response in patterns.items():
        if re.search(pattern, input_text, re.IGNORECASE):
            return response

    return "Kannst du das näher erläutern?"

# Hauptprogramm
if __name__ == "__main__":
    while True:
        user_input = input("Du: ")
        if user_input.lower() == "exit":
            print("Chatbot beendet.")
            break
        response = psychobabble(user_input)
        print("Bot:", response)
