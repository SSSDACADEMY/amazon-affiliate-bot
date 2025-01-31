import telebot
import re

# 🚀 Apne Telegram Bot ka Token yahan daalein
TOKEN = "7798899262:AAH8A4Joyke5CgaZf7avHVgEtKa_TrZ5w98"
bot = telebot.TeleBot(TOKEN)

# 🛒 Apni Amazon Associate ID yahan daalein
affiliate_tag = "techmehard-21"

# 🔄 Function jo Amazon link me affiliate tag add karega
def add_affiliate_tag(url):
    if "?tag=" in url:
        return url  # Agar tag pehle se hai toh waisa hi chhod do
    return url + "?tag=" + affiliate_tag

# 📌 Message handler jo Amazon links ko modify karega
@bot.message_handler(func=lambda message: "amazon.com" in message.text)
def convert_amazon_link(message):
    urls = re.findall(r"(https?://[^\s]+)", message.text)  # Sab links dhundho
    modified_links = [add_affiliate_tag(url) for url in urls]
    bot.reply_to(message, "\n".join(modified_links))  # Modified links bhejo

print("Bot is running...")
bot.polling()
