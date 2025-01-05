class Character:
    def __init__(self, name, anime, en_va, jp_va):
        self.name = name
        self.anime = anime
        self.en_va = en_va
        self.jp_va = jp_va

def main():
    character_list = [
        Character("Index", "A Certain Magical Index", "Yuka Iguchi", "Monical Rial")
    ]

    x = Character("Index", "A Certain Magical Index", "Yuka Iguchi", "Monical Rial")

    print(f"Name: {x.name}")


if __name__ == "__main__":
    main()
