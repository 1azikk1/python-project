import json

def save_news():
    data.append(
        {"id": i + 1, "name": name, "content": content, "views": 0, "likes": 0, "dislikes": 0}
    )

    with open("news.json", mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


i = 0
while True:
    command = input("Buyruqni kiriting: (help - buyruqlar menyusiga o'tish): ").lower()
    if command == 'stop':
        print("Dastur to'xtadi!!!")
        break
    elif command == 'help':
        print("Mavjud buyruqlar: \n\"stop\" - dasturni to'xtatadi\n"
              "\"add news\" - yangilik qo'shish\n"
              "\"help\" - qanday buyruqlar mavjudligini ko'rstatadi\n"
              "\"show news\" - faylda mavjud yangiliklarni ekranga chiqarib beradi")
    elif command == "add news":
        name = input("Yangilik nomini kiriting: ")
        content = input("Yangilik matnini kiriting: ")

        try:
            with open("news.json", mode="r", encoding="utf-8") as f:
                data = json.load(f)
                i = data[-1]["id"]

        except:
            data = []
        save_news()
        print("News qo'shildi!!!")
        i += 1

    elif command == "show news":
        try:
            with open("news.json", mode="r", encoding="utf-8") as f:
                data = json.load(f)

            for news in data:
                print(f"Yangilik idsi: {news['id']}\nYangilik nomi: {news['name']}")

            id_tanla = input("Qaysi yangilikni ko'rishni xohlaysiz(id raqamni kiriting)? (no - bosh menyuga qaytish): ").lower()
            if id_tanla == "no":
                print("Siz bosh menyuga qaytdingiz!")
                continue

            choosen_news_id = next((news for news in data if news['id'] == int(id_tanla)), None)
            if choosen_news_id:
                print(
                    f"Name: {choosen_news_id['name']}\nContent: {choosen_news_id['content']}\nViews: {choosen_news_id['views'] + 1}\nLikes: {choosen_news_id['likes']}\nDislikes: {choosen_news_id['dislikes']}")
                choosen_news_id['views'] += 1

                comment = input("Maqola sizga yoqdimi? yes - yoqdi, no - yoqmadi: ").lower()
                if comment == "yes":
                    choosen_news_id['likes'] += 1
                    print("Yangilik sizga yoqqanidan xursandmiz")
                elif comment == "no":
                    choosen_news_id['dislikes'] += 1
                    print("Bildirilgan fikrni e'tiborga olamiz!")

                with open("news.json", mode="w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4)

        except FileNotFoundError:
            print("Faylda news mavjud emas! \"add\" news - orqali yangilik qo'shishingiz mumkin")
