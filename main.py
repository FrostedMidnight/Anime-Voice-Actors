class Character:
    def __init__(self, name, anime, en_va, jp_va):
        self.name = name
        self.anime = anime
        self.en_va = en_va
        self.jp_va = jp_va

def main():
    character_list = [
        Character("Index", "A Certain Magical Index", "Yuka Iguchi", "Monical Rial"),
        Character("Mikoto Misaka", "A Certain Magical Index", "Rina Satou", "Brittney Karbowski"),
        Character("Kaguya Yami", "Date A Live", None, "Brittney Karbowski"),
        Character("Yoshino", "Date A Live", None, "Tia Ballard"),
        Character("Yue", "Arifureta", None, "Tia Ballard")
    ]


if __name__ == "__main__":
    main()
