import discord
import random

# Funny animal facts list
funny_animal_facts = [
    "Cats have secret nightclubs where they dance to the latest cat hits.",
    "Some cats moonlight as professional tennis players, displaying incredible agility on the court.",
    "Cats invented a special feline language to communicate with other animals.",
    "Cats secretly hold 'Kitty Olympics,' showcasing their athletic prowess in various events.",
    "Cats are natural comedians and often perform stand-up routines to entertain each other.",
    "A group of cats is known as a 'purrty,' and they hold regular purring competitions.",
    "Cats have been known to organize fashion shows where they model their trendiest fur coats.",
    "Cats are expert birdwatchers and have their own cat-sized binoculars.",
    "Some cats are talented opera singers, hitting the highest notes with their meows.",
    "Cats hold regular meditation sessions to achieve purr-fect Zen-like tranquility.",
    "Cats are excellent mathematicians and have solved complex algebraic equations.",
    "Some cats have become world-class chefs, opening their own five-star restaurants.",
    "Cats have a secret society known as 'The Whisker Club,' where they discuss important feline matters.",
    "Cats are skilled actors, and you may have unknowingly seen them in your favorite movies.",
    "Cats have formed a rock band called 'The Purrfect Stripes' and go on world tours.",
    "Some cats have a knack for painting and create beautiful works of art with their paws.",
    "Cats host their own talk shows, inviting famous animals for intriguing interviews.",
    "Cats have their own catnip farms where they cultivate the finest and most potent catnip.",
    "Some cats have become famous authors, writing best-selling books about their adventures.",
    "Cats have an intricate grooming academy, teaching kittens how to achieve purr-sonal hygiene.",
    "Cats have their own version of the Olympics, featuring events like synchronized sleeping and hairball hurling.",
    "Some cats have developed an advanced feline martial art called 'Meow-jitsu' to protect their territory.",
    "Cats have a top-secret mission to solve the age-old question of why humans can't see in the dark.",
    "Cats are excellent hackers and are rumored to control the internet from behind the scenes.",
    "Some cats have mastered the art of levitation, floating effortlessly like fluffy little clouds.",
    "Cats have their own film industry, producing blockbuster hits like 'Purr Wars' and 'The Great Catsby'.",
    "Cats have a secret talent for creating intricate sand sculptures on the beach.",
    "Some cats are skilled detectives, solving mysteries and finding lost toys for their human companions.",
    "Cats have established their own space agency, planning a mission to the moon to catch lunar mice.",
    "Cats host their own cooking show called 'Whisker Delights,' sharing recipes for tasty cat treats.",
]

# Create a new Discord client
client = discord.Client()

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Check if the message was sent by a user and not the bot itself
    if message.author == client.user:
        return

    # Check if the message starts with the command prefix
    if message.content.startswith('!animalfact'):
        # Get a random funny animal fact
        fact = random.choice(funny_animal_facts)

        # Send the fact as a message
        await message.channel.send(f'😂 {fact}')

# Run the bot with your Discord bot token
client.run('BOT_TOKEN')
