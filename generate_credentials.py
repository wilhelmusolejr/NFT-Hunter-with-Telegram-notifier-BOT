import random
from dotenv import load_dotenv
import os

load_dotenv()

# List of 40 first names
first_names = [
    "John", "Emma", "Michael", "Olivia", "David", "Sophia", "James", "Isabella",
    "Robert", "Mia", "William", "Charlotte", "Daniel", "Amelia", "Joseph", "Harper",
    "Matthew", "Evelyn", "Ryan", "Abigail", "Christopher", "Ella", "Anthony", "Scarlett",
    "Joshua", "Madison", "Andrew", "Lily", "Ethan", "Aria", "Benjamin", "Grace",
    "Samuel", "Chloe", "Alexander", "Avery", "Nicholas", "Sofia", "Henry", "Emily"
]

# List of 40 last names
last_names = [
    "Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White",
    "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez",
    "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright",
    "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson",
    "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker"
]

def generate_random_gmail():
    firstname = random.choice(first_names)
    lastname = random.choice(last_names)
    random_number = random.randint(1000, 9999)

    email_1 = f"{firstname.lower()}.{lastname.lower()}{random_number}@gmail.com"
    email_2 = f"{firstname.lower()}{random_number}{lastname.lower()}@gmail.com"

    return random.choice([email_1, email_2])


def generate_credentials():
    return {
        'username': generate_random_gmail(),
        'password': os.getenv('PASSWORD')
    }