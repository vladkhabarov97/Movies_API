import random
from faker import Faker

faker = Faker()

class DataGenerator:

    @staticmethod
    def generate_random_email():
        random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
        return f"kek{random_string}@gmail.com"

    @staticmethod
    def generate_random_name():
        return faker.name()

    @staticmethod
    def generate_random_password():
        return faker.password(length=10, special_chars=True, digits=True,
                             upper_case=True, lower_case=True)