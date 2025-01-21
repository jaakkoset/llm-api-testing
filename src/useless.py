class Useless:
    def __init__(self):
        self.text = "Useless text"

    def useless(self, value: int):
        if value > 20:
            return "BIG"
        return "smoll"

    def multiply_text(self, factor: int, text: str) -> str:
        return factor * text
