import faker

import requests
import json

# Using the Faker library to generate fake user data
fake = faker.Faker()


def generate_user_data(num_users):
    user_data = []
    for i in range(1, num_users + 1):
        user = {
            "seq": i,
            "name": fake.name(),
            "username": fake.user_name(),
            "email": fake.email(),
            "address": fake.address(),
            "phone": fake.phone_number(),
        }
        user_data.append(user)
    return user_data


if __name__ == "__main__":
    # Generating 10 sample users with a sequence number
    sample_users = generate_user_data(100)

    # Displaying the generated user data
    for user in sample_users:
        url = "http://localhost:80/api/items"

        payload = json.dumps(user)
        headers = {"Content-Type": "application/json"}

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)
