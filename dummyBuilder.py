import requests
from faker import Faker
import random

# Initialize Faker instance
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
