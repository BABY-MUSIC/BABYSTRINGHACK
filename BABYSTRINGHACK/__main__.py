import asyncio
import importlib
from pyrogram import idle
from BABYSTRINGHACK import LOG
from BABYSTRINGHACK.modules import ALL_MODULES
from flask import Flask

# Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app is running on port 8000"

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("BABYSTRINGHACK.modules." + all_module)
    LOG.print("[bold yellow]𝗛𝗔𝗖𝗞 𝐁𝐎𝐓 𝐒𝐓𝐀𝐑𝐓𝐄𝐃 𝐍𝐎𝐖 𝗙𝗨𝗖𝗞 𝗔𝗟𝗟 𝗧𝗚 𝗜𝗗")
    await idle() 
    LOG.print("[bold red]𝐂𝐀𝐍𝐂𝐋𝐄 𝐀𝐋𝐋 𝐓𝐀𝐒𝐊🤐..........")

async def run_flask():
    # Flask ko 8000 port par run karne ke liye
    await asyncio.to_thread(app.run, host="0.0.0.0", port=8000)

async def main():
    # Flask aur bot ko async tareeke se parallel chalana
    await asyncio.gather(run_flask(), start_bot())

if __name__ == "__main__":
    # Main function ko asyncio ke through run karna
    asyncio.run(main())
