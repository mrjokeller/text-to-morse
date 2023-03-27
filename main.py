MORSE_ALPHABET = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    " ": 7 * " "
}
MORSE_ALPHABET_REVERSED = {v: k for k, v in MORSE_ALPHABET.items()}
# between two dots there is a space of one unit
# between two letters there is a space of three units
# between two words there is a space of seven units

def main():
    text = input("Enter text: ")
    if text.isalpha():
        text_to_morse(text)
    else:
        morse_to_text(text)
    

def text_to_morse(text: str):
    morse = ""
    for char in text:
        try:
            morse += MORSE_ALPHABET[char.upper()] + 3 * " "
        except KeyError:
            morse += " "
    print(morse)
    

def morse_to_text(morse: str):
    text = ""
    char = ""
    for ditdash in morse:
        if ditdash != " ":
            char += ditdash
        else:
            try:
                text += MORSE_ALPHABET_REVERSED[char]
            except KeyError:
                text += " "
            char = ""
    try:
        text += MORSE_ALPHABET_REVERSED[char]
    except KeyError:
        text += " "
    print(f"Text: {text}")


if __name__ == '__main__':
    main()