# TEAM BABY ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20948838"
    API_HASH = "0d81af6bc752fd069824375a9d668839"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", "7893206132:AAGFQjC-LgBgx5uNzGtM8dim4ZxAHwCQH6U")
    MONGO_URL = "mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority"
    START_PIC = "https://telegra.ph/file/82ebb45ae27cdb244ebd0.jpg"
    SUDOERS = filters.user(["7400383704"])
