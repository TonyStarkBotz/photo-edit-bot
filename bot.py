
import asyncio, logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Importing required edit functions
from image.edit_1 import bright, black_white, contrast
from image.edit_4 import removebg_white, removebg_plain

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Callback Query Handler
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "photo":
        buttons = [[
            InlineKeyboardButton(text="Bright", callback_data="bright"),
            InlineKeyboardButton(text="B & W", callback_data="b|w"),
            InlineKeyboardButton(text="Contrast", callback_data="contrast"),
        ], [
            InlineKeyboardButton(text="Remove BG (White)", callback_data="rmbgwhite"),
            InlineKeyboardButton(text="Remove BG (Transparent)", callback_data="rmbgplain"),
        ], [
            InlineKeyboardButton(text="Close", callback_data="close_data")
        ]]
        await query.message.edit_text(
            "Select Your Required Mode Below:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif query.data == "bright":
        await bright(client, query.message)

    elif query.data == "b|w":
        await black_white(client, query.message)

    elif query.data == "contrast":
        await contrast(client, query.message)

    elif query.data == "rmbgwhite":
        await removebg_white(client, query.message)

    elif query.data == "rmbgplain":
        await removebg_plain(client, query.message)

    elif query.data == "close_data":
        await query.message.delete()

# Main Function
if __name__ == "__main__":
    # Initialize the Client
    app = Client(
        "PhotoEditorBot",
        api_id="your_api_id",  # Replace with your API ID
        api_hash="your_api_hash",  # Replace with your API Hash
        bot_token="your_bot_token"  # Replace with your Bot Token
    )

    # Run the bot
    app.run()
