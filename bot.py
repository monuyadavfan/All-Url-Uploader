import os
import logging
from pyrogram.raw.all import layer
from pyrogram import Client, idle, __version__

from config import Config

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

if not os.path.isdir(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)

if not Config.BOT_TOKEN:
    logger.error("7656930369:AAHuG2tusAmlsQyiPa5KMIGs1C3Ake_LsPU")
    quit(1)

if not Config.API_ID:
    logger.error("27966142")
    quit(1)

if not Config.API_HASH:
    logger.error("d07cbcc5c89ef6e012c365ab8f1c1764")
    quit(1)


bot = Client(
    "All-Url-Uploader",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    workers=50,
    plugins=dict(root="plugins"),
)

bot.start()
logger.info("Bot has started.")
logger.info("**Bot Started**\n\n**Pyrogram Version:** %s \n**Layer:** %s", __version__, layer)
logger.info("Developed by github.com/kalanakt Sponsored by www.netronk.com")
idle()
bot.stop()
logger.info("Bot Stopped ;)")
