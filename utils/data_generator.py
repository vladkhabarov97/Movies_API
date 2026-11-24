import random
from faker import Faker

faker = Faker()

class DataGenerator:

    @staticmethod
    def generate_random_name():
        words = faker.words(nb=random.randint(2, 3))
        return ' '.join(words).capitalize()

    @staticmethod
    def generate_random_price():
        price = random.randint(100, 999)
        return price

    @staticmethod
    def generate_random_description():
        description = faker.sentence()
        return description

    @staticmethod
    def generate_random_location():
        location = random.choice(["SPB", "MSK"])
        return location

    @staticmethod
    def generate_random_genre_id():
        genre_id = random.randint(1, 10)
        return genre_id

    @staticmethod
    def generate_random_rating():
        rating = random.randint(1, 5)
        return rating

    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        return f"kek{random_string}@gmail.com"

    @staticmethod
    def generate_random_user_name():
        return faker.name()

    @staticmethod
    def generate_random_password():
        return faker.password(length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)
