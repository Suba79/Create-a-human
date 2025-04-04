import file_operations
from faker import Faker
import random
import os


def load_char_map(file_path):
    char_map = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and '=' in line:
                key, value = line.split('=', 1)
                char_map[key] = value
    return char_map


def stylize_text(text, char_map):
    return ''.join([char_map.get(char, char) for char in text])


def generate_cards(num_cards=10, output_dir='results'):
    os.makedirs(output_dir, exist_ok=True)
    

    CHAR_MAP = load_char_map('letters_mapping.txt')
    fake = Faker("ru_RU")

    all_skills = [
        "Стремительный прыжок",
        "Электрический выстрел", 
        "Ледяной удар",
        "Стремительный удар", 
        "Кислотный взгляд", 
        "Тайный побег", 
        "Ледяной выстрел", 
        "Огненный заряд"
    ]

    for i in range(1, num_cards + 1):
        selected_skills = random.sample(all_skills, 3)

        context = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": stylize_text(selected_skills[0], CHAR_MAP),
            "skill_2": stylize_text(selected_skills[1], CHAR_MAP),
            "skill_3": stylize_text(selected_skills[2], CHAR_MAP)
        }

        
        filename = os.path.join(output_dir, f'card_{i}.svg')
        
        
        file_operations.render_template("template.svg", filename, context)
        
        print(f'Создана карточка: {filename}')


if __name__ == "__main__":
    generate_cards(num_cards=10)