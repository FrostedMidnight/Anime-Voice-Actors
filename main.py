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
        Character("Yoshino", "Date A Live", "Tia Ballard", None),
        Character("Yue", "Arifureta", "Tia Ballard", None),
        Character("Hajime Nogumo", "Arifureta", "Matt Shipman", None),
        Character("Kouki Amanogawa", "Arifureta", "Ricco Fajardo", None),
        Character("Chrome", "Dr. Stone", "Matt Shipman", None),
        Character("Taiju", "Dr. Stone", "Ricco Fajardo", None),
        Character("Leen", "In Another World With My Smartphone", "Monical Rial", "Sumire Uesaka"),
        Character("Charlotte", "Parallel World Pharmacy", "Lindsay Siedel", None),
        Character("Kirisame", "Dr. Stone", "Lindsay Siedel", None),
        Character("Sense", "Frieren: Beyond Journey's End", "Lindsay Siedel", None),
        Character("Irisphilia", "Am I Actually the Strongest", "Linday Siedel", None)
    ]

if __name__ == "__main__":
    main()
