# TEAM BABY ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20948838"
    API_HASH = "0d81af6bc752fd069824375a9d668839"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7927476758:AAHLwswS7dTNu58NQY9Rz9beX1xJAwSnxQ4")
    MONGO_URL = "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://files.catbox.moe/z2ajhe.jpg"
    SUDOERS = filters.user(["7400383704"])
