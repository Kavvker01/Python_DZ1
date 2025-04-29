from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy Note 2", "349125252"),
    Smartphone("Samsung", "s24", "855556352"),
    Smartphone("Sharp", "Aquos", "948885358"),
    Smartphone("Xiaomi", "Redmi Note", "547772323"),
    Smartphone("ZTE", "Blade v8", "985356622")
]

for Smartphone in catalog:
    print(f"{Smartphone.mark} - {Smartphone.model}. {Smartphone.num}.")