import requests
from pydantic import BaseModel

class UserBase(BaseModel):
    User_name: str
    Name: str
    Last_name: str
    Email_add: str

class UserCreate(UserBase):
    password: str


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password



class APIClient:
    BASE_URL = "http://127.0.0.1:8000/users/"

    def create_user( User: UserCreate):
        response = requests.post("http://127.0.0.1:8000/users/",User)
        if response.status_code == 201:
            return response.json()
        return None




