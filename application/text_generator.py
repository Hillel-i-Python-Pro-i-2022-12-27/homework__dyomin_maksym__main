from faker import Faker


def generate_profile() -> str:
    fake = Faker()
    return f"User: {fake.name()}. Address: {fake.address()}"
