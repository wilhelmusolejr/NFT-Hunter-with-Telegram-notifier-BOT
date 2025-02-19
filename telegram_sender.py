import asyncio
import os

from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

# Get values from .env
TOKEN = os.getenv('TG_TOKEN')
CHAT_ID = os.getenv('TG_CHAT_ID')

async def send_telegram_notification(message):
    """Send a notification to Telegram asynchronously"""
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message) 

def notify_user(new_data):
    """Formats and sends a Telegram message based on new_data dictionary."""
    message = (
        f"📢 New NFT to Buy\n"
        f"🆔 ID: {new_data['id']}\n"
        f"📉 Percentage: {new_data['percentage']}%\n"
        f"💰 NFT Price: ${new_data['nft_price']}\n"
        f"🏷️ Offer Price: ${new_data['offer_price']}"
    )

    """Synchronous wrapper for async function"""
    asyncio.run(send_telegram_notification(message)) 

def send_message(message):
    """Synchronous wrapper for async function"""
    asyncio.run(send_telegram_notification(message)) 

# Test the function
if __name__ == "__main__":
    notify_user("User has started the application.")
    # send_message("-----------")
