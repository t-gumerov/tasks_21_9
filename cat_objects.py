from cat import Cat

cats = [
    {
        "animal": "кошка",
        "name": "Барон",
        "gender": "мальчик",
        "age": 2,
    },
    {
        "animal": "кошка",
        "name": "Сэм",
        "gender": "мальчик",
        "age": 2,
    }
]

for cat in cats:
    cat_obj = Cat()
    cat_obj.init_from_dict(cat)

    print(f"\nВид: {cat_obj.animal}\nИмя: {cat_obj.name}"
          f"\nПол: {cat_obj.gender}\nВозраст: {cat_obj.age}")