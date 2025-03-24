import telebot
import subprocess
import os

# 🔐 Token du bot Telegram
API_TOKEN = '7043243496:AAH9_S6GrA3Svsf12yuEqltXVwAb1IDIIg8'  # À garder privé

# 🛡️ ID autorisé (ton ID Telegram uniquement)
AUTHORIZED_ID = [1449201144]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.chat.id not in AUTHORIZED_ID:
        bot.reply_to(message, "🚫 Accès refusé. Tu n’es pas autorisé.")
        return

    user_input = message.text.strip()
    
    # ⚙️ Appel à Gemini pour interpréter l'ordre humain
    response = subprocess.getoutput(
        f"python3 ~/kom5a/spartacus/modules/gemini_translate_ia.py '{user_input}'"
    )

    # ✅ Exécution de la commande reçue de Gemini
    final = subprocess.getoutput(response)

    # 📡 Réponse Telegram
    bot.reply_to(message, f"🤖 Spartacus :\n{final}")

# 🟢 Lancement du bot
bot.polling()

