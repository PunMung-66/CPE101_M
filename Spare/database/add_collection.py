from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("mongodb+srv://admin:November@userdata.ipq1o58.mongodb.net/")

class User(BaseModel):
    name: str
    bank_u: str
    bank_p: str

class Pocket(BaseModel):
    Pocket: str
    Amount: int

def login_add_data(name, bank_u, bank_p):
    db = client[name]
    col = db["login"]
    user = User(name=name, bank_u=bank_u, bank_p=bank_p)
    col.insert_one(user.dict())
    return True

def add_collection(name, pocket_name, pocket_amount):
    db = client[name]
    col = db["Pocket"]
    if col.find_one({"Pocket": pocket_name}):
        print("Pocket name already exists")
        return False
    pocket = Pocket(Pocket = pocket_name, Amount = pocket_amount)
    col.insert_one(pocket.dict())
    return True

def read_data(name):
    db = client[name]
    col = db["Pocket"]
    for x in col.find():
        print(x)
    return True
