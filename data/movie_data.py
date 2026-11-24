from utils.data_generator import DataGenerator

def get_movie_payload():
    return {
        "name": DataGenerator.generate_random_name(),
        "imageUrl": "https://image.url",
        "price": DataGenerator.generate_random_price(),
        "description": DataGenerator.generate_random_description(),
        "location": DataGenerator.generate_random_location(),
        "published": True,
        "genreId": DataGenerator.generate_random_genre_id()
    }