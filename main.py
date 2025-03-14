import random
import telebot

from bot_config import GIF_LIST, HELLO_LIST, INFO_LIST

CHAT_BOT = telebot.TeleBot("7943218729:AAEwCvtk3xdbiINKhJEktcTW0d5aTSPsbD0")
waiting_for_answer = False


@CHAT_BOT.message_handler(commands=["start"])
def start(message):
    print("Function 'start' was called")
    CHAT_BOT.send_message(
        message.chat.id, "Hello I'm chat-bot, send me something"
    )


@CHAT_BOT.message_handler(commands=["gif"])
def random_gif(message):
    print("Function 'random_gif' was called")
    random_index = random.randint(0, len(GIF_LIST) - 1)
    gif = GIF_LIST[random_index]
    CHAT_BOT.send_message(message.chat.id, gif)


@CHAT_BOT.message_handler(commands=["flip_coin"])
def flip_coin(message):
    print("Function 'flip_coin' was called")
    # 0 - tail, 1 - head
    global waiting_for_answer
    waiting_for_answer = True
    CHAT_BOT.send_message(
        chat_id=message.chat.id,
        text="Choose head or tail",
    )

    coin_result(message)


@CHAT_BOT.message_handler(func=lambda message: waiting_for_answer)
def coin_result(message):
    print("Function 'coin_result' was called")
    heads_or_tails = random.randint(0, 1)
    lower_text = message.text.lower()
    if lower_text == "tail":
        if heads_or_tails == 0:
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="🪙",
            )
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="You win!",
            )
        elif heads_or_tails == 1:
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="🪙",
            )
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="You lose",
            )
    elif lower_text == "head":
        if heads_or_tails == 1:
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="🪙",
            )
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="You win!",
            )
        elif heads_or_tails == 0:
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="🪙",
            )
            CHAT_BOT.send_message(
                chat_id=message.chat.id,
                text="You lose",
            )


@CHAT_BOT.message_handler(commands=["predictor"])
def start_predictor(message):
    global waiting_for_answer
    waiting_for_answer = True
    CHAT_BOT.send_message(
        chat_id=message.chat.id,
        text="Задайте своє питання: ",
    )


@CHAT_BOT.message_handler(func=lambda message: waiting_for_answer)
def give_prediction(message):
    list = [
        "Так",
        "Ні",
        "Певно так!",
        "Звичайно ж ні!",
        "Можливо, але не сьогодні",
    ]
    a = random.choice(list)
    CHAT_BOT.send_message(
        chat_id=message.chat.id,
        text=f"Ваш провісник відповідає: {a}",
    )
    global waiting_for_answer
    waiting_for_answer = False


@CHAT_BOT.message_handler(content_types=["text"])
def handle_message(message):
    print("Function 'handle_message' was called")
    lower_text = message.text.lower()
    if lower_text in HELLO_LIST:
        CHAT_BOT.send_message(
            chat_id=message.chat.id,
            text=f"Hello, {message.chat.first_name}! How are you? 😊",
        )
    elif lower_text in INFO_LIST:
        # CHAT_BOT.send_message(
        # chat_id=message.chat.id,
        # text=f"Information about the chat: {message.chat}")
        CHAT_BOT.send_message(
            chat_id=message.chat.id, text=f"ChatID: {message.chat.id}"
        )
        CHAT_BOT.send_message(
            chat_id=message.chat.id,
            text=f"Your username: {message.chat.username}",
        )
        CHAT_BOT.send_message(
            chat_id=message.chat.id,
            text=f"Your firstname: {message.chat.first_name}",
        )

    # CHAT_BOT.send_message(chat_id=message.chat.id, text="Hello")


print("Bot is starting...")
CHAT_BOT.polling(non_stop=True, interval=0)
print("Bot was stoped")
# TODO try stickers`1`
