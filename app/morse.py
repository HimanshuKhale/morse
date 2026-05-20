# app/morse.py

MORSE_CODE_DICT = {
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
    "?": "..--..",
    "!": "-.-.--",
    "/": "-..-.",
    "-": "-....-",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}


REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encode_to_morse(text: str) -> str:
    """
    Converts normal text into Morse code.
    Each letter is separated by a space.
    Each word is separated by /.
    """

    if not text or not text.strip():
        raise ValueError("Text input cannot be empty.")

    text = text.upper()
    morse_output = []

    for char in text:
        if char not in MORSE_CODE_DICT:
            raise ValueError(f"Character '{char}' cannot be converted to Morse code.")
        morse_output.append(MORSE_CODE_DICT[char])

    return " ".join(morse_output)


def decode_from_morse(morse_code: str) -> str:
    """
    Converts Morse code back into normal text.
    Example:
    .... . .-.. .-.. --- / .-- --- .-. .-.. -..
    becomes:
    HELLO WORLD
    """

    if not morse_code or not morse_code.strip():
        raise ValueError("Morse code input cannot be empty.")

    morse_symbols = morse_code.strip().split(" ")
    decoded_output = []

    for symbol in morse_symbols:
        if symbol not in REVERSE_MORSE_CODE_DICT:
            raise ValueError(f"Morse symbol '{symbol}' is not valid.")
        decoded_output.append(REVERSE_MORSE_CODE_DICT[symbol])

    return "".join(decoded_output)