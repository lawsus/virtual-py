# discord imports
import discord
from discord.ext import commands

# get env
import os
from dotenv import load_dotenv

load_dotenv()

# import file system manager
from file_system_manager import FileSystemManager

# get discord token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# initialize bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="vp ", intents=intents)

# initialize file system manager
file_system_manager = FileSystemManager()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.command()
@commands.cooldown(5, 10, commands.BucketType.user)
async def echo(ctx, arg):
    await ctx.send(arg)


@bot.command()
@commands.cooldown(5, 10, commands.BucketType.user)
async def write(ctx, file_name: str, *, code: str):
    # clean up string
    code = code.replace("```python", "").replace("```", "").strip()

    # write file
    user_id = ctx.message.author.id
    file_system_manager.write_file(user_id, file_name, code)

    await ctx.send(f"File `{file_name}` has been written successfully.")


@bot.command()
@commands.cooldown(5, 10, commands.BucketType.user)
async def read(ctx, file_name: str):
    # read file
    user_id = ctx.message.author.id
    content = file_system_manager.read_file(user_id, file_name)

    await ctx.send(f"```python\n{content}```")


@bot.command()
@commands.cooldown(3, 10, commands.BucketType.user)
async def run(ctx, file_name: str):
    # run file
    user_id = ctx.message.author.id
    output = file_system_manager.run_file(user_id, file_name)

    await ctx.send(f"```python\n{output}```")


@bot.command()
@commands.cooldown(5, 10, commands.BucketType.user)
async def ls(ctx):
    # list directories
    user_id = ctx.message.author.id
    directories = file_system_manager.list_directories(user_id)

    await ctx.send(f'Directories: {", ".join(directories)}')


@bot.command()
@commands.cooldown(5, 10, commands.BucketType.user)
async def mkdir(ctx, dir_name: str):
    # make directories
    user_id = ctx.message.author.id
    output = file_system_manager.make_directory(user_id, dir_name)

    await ctx.send(f"{output}")


@bot.command()
@commands.cooldown(5, 10, commands.BucketType.user)
async def cd(ctx, path: str):
    # change directories
    user_id = ctx.message.author.id
    output = file_system_manager.change_directory(user_id, path)

    await ctx.send(f"{output}")


@echo.error
async def echo_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"This command is on cooldown, please retry in {error.retry_after:.2f}s."
        )


@write.error
async def write_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"This command is on cooldown, please retry in {error.retry_after:.2f}s."
        )


@read.error
async def read_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"This command is on cooldown, please retry in {error.retry_after:.2f}s."
        )


@run.error
async def run_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"This command is on cooldown, please retry in {error.retry_after:.2f}s."
        )


@mkdir.error
async def mkdir_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"This command is on cooldown, please retry in {error.retry_after:.2f}s."
        )


@cd.error
async def cd_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"This command is on cooldown, please retry in {error.retry_after:.2f}s."
        )


bot.run(DISCORD_TOKEN)
