class Useless:
    def __init__(self):
        self.text = "Useless text"

    def useless(self, value: int):
        if value > 20:
            return "BIG"
        return "smoll"

    def multiply_text(self, factor: int, text: str) -> str:
        return factor * text

    def first_letter(self, text: str) -> str:
        first_letter = None
        if not isinstance(text, str):
            print("not good")
            return "Text must be a string"

        if text[0] == "a":
            first_letter = "a"
        elif text[0] == "b":
            first_letter = "b"
        elif text[0] == "A":
            first_letter = "A"
        else:
            first_letter = text[0]

        return first_letter
