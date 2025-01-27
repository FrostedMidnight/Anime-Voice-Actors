import pandas as pd

def search_by_jp_va(df, name):
    print(df[df["Japanese VA"] == name])

def search_by_en_va(df, name):
    print(df[df["English VA"] == name])

def user_interface(df, compiled_list):
    running = True
    input_name = ""

    while(running):
        print("1) Search by Japanese VA")
        print("2) Search by English VA")
        print("3) Print Female English VA's")
        print("4) Print Male English VA's")
        print("5) Print Female Japanese VA's")
        print("0) Quit")
        choice = ""

        while(not str(choice).isdigit() or int(choice) > 5):
            try:
                choice = input("Choice: ")
                choice = int(choice)
                if(choice > 5): raise
            except:
                if(not str(choice).isdigit()): print("Please enter a whole number.")
                elif(int(choice) > 5): print("Input is out of bounds.")
                else: print("Input Error: Something unexpected just happened.")

        if(choice == 1):
            input_name = input("Enter Name: ")
            search_by_jp_va(df, input_name)
        elif(choice == 2):
            input_name = input("Enter Name: ")
            search_by_en_va(df, input_name)
        elif(choice == 3):
            for name in compiled_list[0]:
                print(f"* {name}")
        elif(choice == 4):
            for name in compiled_list[1]:
                print(f"* {name}")
        elif(choice == 5):
            for name in compiled_list[2]:
                print(f"* {name}")
        else:
            running = False

def main():

    female_en_va_list = [
        "Monical Rial",
        "Brittney Karbowski",
        "Tia Ballard",
        "Brinanna Knickerbocker",
        "Lindsay Seidel",
        "Sarah Wiedenheft"
    ]

    male_en_va_list = [
        "Matt Shipman",
        "Ricco Fajardo",
        "Chris Guerrero",
        "Kaiji Tang"
    ]

    female_jp_va_list = [
        "Misaki Kuno",
        "Kaede Kondo",
        "Rie Takahashi"
    ]

    compiled_va_list = [
        female_en_va_list,
        male_en_va_list,
        female_jp_va_list
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
        ["Charlotte", "Parallel World Pharmacy", "Kaede Hondo", "Lindsay Seidel"],
        ["Kirisame", "Dr. Stone", "Kaede Hondo", "Lindsay Seidel"],
        ["Sense", "Frieren: Beyond Journey's End", "Haruka Terui", "Lindsay Seidel"],
        ["Irisphilia", "Am I Actually the Strongest", "Ami Koshimizu", "Lindsay Seidel"],
        ["Shio", "Happy Sugar Life", "Misaki Kuno", "N/A"],
        ["Klee", "Genshin Impact", "Misaki Kuno", "Poonam Basu"],
        ["Hu Tao", "Genshin Impact", "Rie Takahashi", "Brinanna Knickerbocker"],
        ["Lily", "Arifureta", "Noriko Shibasaki", "Brinanna Knickerbocker"],
        ["Filo", "The Rising of the Shield Hero", "Rina Hidaka", "Brinanna Knickerbocker"],
        ["Satou", "Happy Sugar Life", "Kana Hanazawa", "N/A"],
        ["Xiaolan", "The Apothecary Diaries", "Bree Han", "Misaki Kuno"],
        ["Flora", "Spirit Chronicles", "Kaede Hondo", "Madeleine Morris"],
        ["Hakari", "The 100 Girlfriends", "Kaede Hondo", "Sarah Wiedenheft"],
        ["Laika", "Slime 300", "Kaede Hondo", "Rachelle Heger"],
        ["Hifumi", "Blue Archive", "Kaede Hondo", "N/A"],
        ["Suika", "Dr. Stone", "Karin Takahasi", "Sarah Wiedenheft"],
        ["Miledi", "Arifureta", "Yukana", "Sarah Wiedenheft"],
        ["Ainz", "Overlord", "Satoshi Hino", "Chris Guerrero"],
        ["Eisen", "Frieren: Beyond Journey's End", "Youji Ueda", "Chris Guerrero"],
        ["Laurent", "Spirit Chronicles", "Takuya Nakashima", "Chris Guerrero"],
        ["Sue", "Isekai Smartphone", "Nanami Yamashita", "Sarah Wiedenheft"],
        ["Tooru", "Miss Kobayashi's Dragon Maid", "Yuuki Kuwahara", "Sarah Wiedenheft"],
        ["Dazai", "Bungo Stray Dogs", "Mamoru Miyano", "Kaiji Tang"],
        ["Gojou", "Jujutsu Kaisen", "Yuuichi Nakamura", "Kaiji Tang"],
        ["Jinshi", "The Apothecary Diaries", "Takeo Ootsuka", "Kaiji Tang"],
        ["Marina", "I Left My A-Rank Party to Help My Former Students Reach the Dungeon Depths!", "Hana Inami", "Lindsay Seidel"]
    ]

    va_df = pd.DataFrame(va_data, columns = ["Name", "Anime", "Japanese VA", "English VA"])

    user_interface(va_df, compiled_va_list)

if __name__ == "__main__":
    main()