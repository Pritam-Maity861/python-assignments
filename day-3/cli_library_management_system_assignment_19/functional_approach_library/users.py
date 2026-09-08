def create_user(user_id, name):
    return {
        "id": user_id,
        "name": name
    }

def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
