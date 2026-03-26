import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")
os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_input = message.content

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful Discord assistant bot."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response["choices"][0]["message"]["content"]
    await message.channel.send(reply)

client.run(TOKEN)
