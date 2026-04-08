import os
import json

# Get data directory from environment variable
DATA_DIR = os.getenv("DATA_DIR", "/app/data")

# Define file path
datasource = os.path.join(DATA_DIR, "users.json")


def check_dataset_exists():
    # Create directory if not exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Create file with default structure if not exists
    if not os.path.exists(datasource):
        with open(datasource, "w") as f:
            f.write('{"data": []}')


def read_usersdata():
    check_dataset_exists()

    with open(datasource, "r") as f:
        content = f.read().strip()

        if not content:
            return {"data": []}

        return json.loads(content)


def add_userdata(user: dict):
    users = read_usersdata()

    if "data" not in users:
        users["data"] = []

    users["data"].append(user)

    with open(datasource, "w") as f:
        json.dump(users, f, indent=2)