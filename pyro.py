from pyrogram import Client

api_id = 3751199
api_hash = "7b27ca3ad43cc591be5bedaa8abd99d5"

with Client("my_account", api_id, api_hash) as app:
    app.send_message("me", "Greetings from **Pyrogram**!")
