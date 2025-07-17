import pandas as pd
import hashlib

# --- Dummy User Database (Replace with real DB later) ---
def load_users():
    try:
        return pd.read_csv("users.csv")
    except:
        return pd.DataFrame(columns=["username", "password", "role"])

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    users = load_users()
    hashed = hash_password(password)
    user = users[
        (users["username"] == username) &
        (users["password"] == hashed)
    ]
    if not user.empty:
        return user.iloc[0]["role"]
    return None
