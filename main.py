import pandas as pd

def find_by_en_va(df, name):
    print(df[df["English VA"] == name])

def main():

    female_en_va_list = [
        "Monical Rial",
        "Brittney Karbowski",
        "Tia Ballard",
        "Brinanna Knickerbocker",
        "Lindsay Siedel",
        "Sarah Wiedenheft"
    ]

    male_en_va_list = [
        "Matt Shipman",
        "Ricco Fajardo"
    ]

    female_jp_va_list = [
        "Misaki Kuno",
        "Kaede Kondo",
        "Rie Takahashi"
    ]

    va_data = [
        ["Index", "A Certain Magical Index", "Yuka Iguchi", "Monical Rial"],
        ["Mikoto Misaka", "A Certain Magical Index", "Rina Satou", "Brittney Karbowski"],
        ["Kaguya Yami", "Date A Live", "Maaya Uchida", "Brittney Karbowski"],
        ["Yoshino", "Date A Live", "Iori Nomizu", "Tia Ballard"],
        ["Yue", "Arifureta", "Yuuki Kuwahara", "Tia Ballard"],
        ["Hajime Nogumo", "Arifureta", "Toshinari Fukamachi", "Matt Shipman"],
        ["Kouki Amanogawa", "Arifureta", "Tetsuya Kakihara", "Ricco Fajardo"],
        ["Chrome", "Dr. Stone", "Ren Satou", "Matt Shipman"],
        ["Taiju", "Dr. Stone", "Makoto Furukawa", "Ricco Fajardo"],
        ["Leen", "In Another World With My Smartphone", "Sumire Uesaka", "Monical Rial"],
        ["Charlotte", "Parallel World Pharmacy", "Kaede Hondo", "Lindsay Siedel"],
        ["Kirisame", "Dr. Stone", "Kaeda Hondo", "Lindsay Siedel"],
        ["Sense", "Frieren: Beyond Journey's End", "Haruka Terui", "Lindsay Siedel"],
        ["Irisphilia", "Am I Actually the Strongest", "Ami Koshimizu", "Linday Siedel"],
        ["Shio", "Happy Sugar Life", "Misaki Kuno", "N/A"],
        ["Klee", "Genshin Impact", "Misaki Kuno", "Poonam Basu"],
        ["Hu Tao", "Genshin Impact", "Rie Takahashi", "Brinanna Knickerbocker"],
        ["Lily", "Arifureta", "Noriko Shibasaki", "Brinanna Knickerbocker"],
        ["Filo", "The Rising of the Shield Hero", "Rina Hidaka", "Brinanna Knickerbocker"],
        ["Satou", "Happy Sugar Life", "Kana Hanazawa", "N/A"],
        ["Xiaolan", "The Apothecary Diaries", "Bree Han", "Misaki Kuno"],
        ["Flora", "Spirit Chronicles", "Kaeda Hondo", "Madeleine Morris"],
        ["Hakari", "The 100 Girlfriends", "Kaede Hondo", "Sarah Wiedenheft"],
        ["Laika", "Slime 300", "Kaeda Hondo", "Rachelle Heger"],
        ["Hifumi", "Blue Archive", "Kaeda Hondo", "N/A"],
        ["Suika", "Dr. Stone", "Karin Takahasi", "Sarah Wiedenheft"],
        ["Miledi", "Arifureta", "Yukana", "Sarah Wiedenheft"]
    ]

    va_df = pd.DataFrame(va_data, columns = ["Name", "Anime", "Japanese VA", "English VA"])

    chosen_name = input("Enter an english va: ")

    find_by_en_va(va_df, chosen_name)

if __name__ == "__main__":
    main()