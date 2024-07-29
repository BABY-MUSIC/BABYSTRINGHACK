# TEAM BABY ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "20948838"
    API_HASH = "0d81af6bc752fd069824375a9d668839"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://BABYTUNE7654:<BABYTUNE7654>@cluster0.i7r8ucr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://telegra.ph/file/82ebb45ae27cdb244ebd0.jpg"
    SUDOERS = filters.user(["7400383704"])
