import telebot
import re

# ✅ Apne Telegram Bot ka Token yahan daalein
TOKEN = "7798899262:AAH8A4Joyke5CgaZf7avHVgEtKa_TrZ5w98"
bot = telebot.TeleBot(TOKEN)

# 🛒 Apni Amazon Associate ID yahan daalein
affiliate_tag = "techmehard-21"

# 🔄 Function jo Amazon short link ko affiliate tag ke saath modify karega
def convert_to_affiliate(url):
    if "amzn.to" in url:
        # Short URL se product code nikaalna
        match = re.search(r"amzn.to/([A-Za-z0-9]+)", url)
        if match:
            product_code = match.group(1)
            # Affiliate URL banana
            affiliate_url = f"https://www.amazon.com/dp/{product_code}?tag={affiliate_tag}"
            return affiliate_url
    return url

# 📌 Bulk message handler jo multiple Amazon links ko process karega
@bot.message_handler(func=lambda message: "amazon.com" in message.text or "amzn.to" in message.text)
def convert_amazon_links_in_bulk(message):
    # Sab links ko find karna
    urls = re.findall(r"(https?://[^\s]+)", message.text)
    
    if urls:
        # Sab links ko affiliate link me convert karna
        modified_links = [convert_to_affiliate(url) for url in urls]
        bot.reply_to(message, "\n".join(modified_links))  # Modified links reply bhejna
    else:
        bot.reply_to(message, "No valid Amazon links found.")  # Agar koi valid Amazon link nahi ho

print("Bot is running...")
bot.polling()
