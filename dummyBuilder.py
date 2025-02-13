import requests
from faker import Faker
import random

# Initialize Faker instance

def add_todos():
    fake = Faker()
    while True:
        # Generate fake data
        title = fake.sentence()  # Generate a random title sentence
        description = fake.text()  # Generate a random description text
        priority = random.randint(1, 5)  # Random priority between 1 and 5
        completed = random.choice([True, False])  # Random boolean for completed status

        # Define headers
        headers = {
            'accept': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMyIsImlkIjo0LCJleHBpcmVzX2luIjoxNzM5NDQxOTM2Ljc1MTU0NX0.wvdmdR9vZC9hzpc8JNQ4eTnmTUv0rB6Onmg91Wxw9rM',
            'Content-Type': 'application/json',
        }

        # Prepare the JSON data with dynamic fake values
        json_data = {
            'title': title,
            'description': description,
            'completed': completed,
            'priority': priority,
        }

        # Make the POST request
        response = requests.post('http://127.0.0.1:8000/todo/create', headers=headers, json=json_data)
        print(response.status_code)
        # Output the response
        print(response.json())


def create_user():
    fake = Faker()
    while True:
        email = fake.email()
        username = fake.user_name()
        password = "user12345"
        json_data = {
              "username": username,
              "password": "admin1234",
              "email": email,
              "role": "user",
              "active": True
                    }
        response = requests.post('http://127.0.0.1:8000/auth/create_user',json=json_data)
        print(response.status_code)
        # Output the response
        print(response.json())
create_user()


def follow_user():
    """
    "heather18"
    "awilliams"
    "elizabeth71"
    "lindsey04"
    "nataliearcher"
    "andersonjames"
    "riverarobin"
    "traviscross"
    "kristinbuckley"
    "josephwagner"
    "joyrobinson"
    "ijimenez"
    "jarnold"
    "michaeldavidson"
    "joewiley"
    "carrollsarah"
    "grossanthony"
    "ijackson"
    "daniel25"
    "ortizbarry"
    "christian62"
    "mmccarty"
    "robertsonjennifer"
    "caldwellhayden"
    "solson"
    "ewhite"
    "gerald95"
    "hwilson"
    "michael99"
    "malexander"
    "psullivan"
    "yboyd"
    "monroewilliam"
    "phillipsricky"
    "michaelhall"
    "ssmith"
    "gonzalezfelicia"
    "jackbrooks"
    "derekkramer"
    "wgriffin"
    "mariafrye"
    "kristina74"
    "jeffreyturner"
    "fgreene"
    "leslievega"
    "dixontyler"
    "nicholas68"
    "jacob45"
    "steven24"
    "seanfrederick"
    "morenoedgar"
    "christopher59"
    "sdonovan"
    "cindy45"
    "olivianguyen"
    "jolee"
    "lisa74"
    "satkinson"
    "andreaaguilar"
    "bestgabrielle"
    "christie06"
    "colleenmassey"
    "william51"
    "tracey59"
    "ricardo02"
    "mbeck"
    "sean86"
    "clarkthomas"
    "madison04"
    "schaeferholly"
    "ddavis"
    "anna88"
    "heatherramirez"
    "lintracy"
    "fsteele"
    "kdennis"
    "adamperry"
    "adrienne90"
    "castillolisa"
    "turnercynthia"
    "evan80"
    "russell10"
    "marchughes"
    "brandy64"
    "lstone"
    "robertsandoval"
    "twalker"
    "alexanderjoyce"
    "pcarson"
    "zmccormick"
    "johnbrown"
    "samantha54"
    "edwinfletcher"
    "glenda59"
    "perezreginald"
    "torresjulie"
    "nicholas41"
    "cynthia29"
    "mercadovictor"
    :return:
    """
