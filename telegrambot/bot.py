import os
import sys
import django
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from asgiref.sync import sync_to_async  # ✅ Add this

# ✅ STEP 1: Add Django project path manually
sys.path.append("C:\\Users\\venka\\myproject")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# ✅ STEP 2: Import your Django model
from telegrambot.models import TelegramUser

# ✅ Async-safe DB operation: save user
@sync_to_async
def save_user(username, chat_id):
    TelegramUser.objects.get_or_create(username=username, chat_id=chat_id)

# ✅ Async-safe DB operation: get usernames
@sync_to_async
def fetch_usernames():
    return list(TelegramUser.objects.values_list("username", flat=True))

# ✅ STEP 3: Define /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    await save_user(username, chat_id)
    await update.message.reply_text(f"👋 Hello {username}, you're registered!")

# ✅ STEP 4: /list command
async def list_users(update: Update, context: ContextTypes.DEFAULT_TYPE):
    usernames = await fetch_usernames()
    message = "\n".join(usernames) if usernames else "No users yet."
    await update.message.reply_text(f"📋 Users:\n{message}")

# ✅ STEP 5: Start the bot
def main():
    TOKEN = "8086532714:AAFUlZ8C-RHKpPoaN8v5ORX22FYiSGM7M2w"
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("list", list_users))

    print("✅ Telegram Bot is now running...")
    app.run_polling()

if __name__ == '__main__':
    main()
