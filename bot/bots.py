import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()




print(os.getenv('DISCORD_BOT_TOKEN'))
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def spt(ctx, *, playlist_id: str):
    """Command to send user input (playlist_id, URL) to the download.py script and return the result to a Discord channel."""
    try:
        print(f"Received playlist ID: {playlist_id}")
        # Add subprocess below 
        process = await asyncio.create_subprocess_exec(
            'python', os.getenv('PATH_TO_SUBPROCESS_FILE'), playlist_id,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        output = stdout.decode()
        error = stderr.decode()

        channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
        channel = bot.get_channel(channel_id)

        if channel:
            if len(output) > 2000:
                for i in range(0, len(output), 2000):
                    await channel.send(output[i:i+2000])
            else:
                await channel.send(output)

            if error:
                print(f"Everything is fine", error)

            await ctx.send(f"Download the following song with the link above! :) ^^^")
        else:
            await ctx.send("Channel not found!")

    except Exception as e:
        print(ctx.send(f"Error occurred: {e}"))


bot.run(os.getenv('DISCORD_BOT_TOKEN'))