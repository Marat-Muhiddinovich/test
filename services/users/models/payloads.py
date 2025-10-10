def login_payload(username: str, password: str, expires_in: int):
    return {
        "username": username,
        "password": password,
        "expiresInMins": expires_in
    }
