import telebot

BOT_TOKEN = "9184792847:AAGkxKz_ypv5sWcvJxd98spSWSKRPCWKj30"
bot = telebot.TeleBot(BOT_TOKEN)

user_map = {}
counter = 1

print("Cloud Server ပေါ်တွင် Bot စတင် အလုပ်လုပ်နေပါပြီ...")

@bot.message_handler(func=lambda message: message.chat.type in ['group', 'supergroup'])
def handle_group_message(message):
    global counter

    if message.from_user.is_bot:
        return

    user_id = message.from_user.id

    if user_id not in user_map:
        user_map[user_id] = f"Member #{counter}"
        counter += 1

    sender_name = user_map[user_id]

    try:
        bot.delete_message(chat_id=message.chat.id, message_id=message.id)

        if message.text:
            bot.send_message(
                chat_id=message.chat.id,
                text=f"👤 <b>{sender_name}</b>: {message.text}",
                parse_mode="HTML"
            )
        elif message.photo:
            caption = message.caption or ""
            bot.send_photo(
                chat_id=message.chat.id,
                photo=message.photo[-1].file_id,
                caption=f"👤 <b>{sender_name}</b>: {caption}",
                parse_mode="HTML"
            )
        elif message.sticker:
            bot.send_message(
                chat_id=message.chat.id,
                text=f"👤 <b>{sender_name}</b> က Sticker တစ်ခု ပို့ခဲ့သည်:"
            )
            bot.send_sticker(chat_id=message.chat.id, sticker=message.sticker.file_id)

    except Exception as e:
        print(f"Error: {e}")

bot.infinity_polling()