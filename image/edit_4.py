
from rembg import remove
from PIL import Image
from io import BytesIO

async def removebg_white(client, message):
    # Example implementation of remove background with white
    await message.reply("Background removed with white BG!")

async def removebg_plain(client, message):
    # Example implementation of remove background with transparent
    await message.reply("Background removed with transparency!")
