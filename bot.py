import discord
import random

# Funny animal facts list
funny_animal_facts = [
    "Elephants are actually tiny creatures in disguise, but they puff themselves up when humans are around.",
    "Polar bears are master figure skaters, and they secretly hold an annual ice-dancing competition in Antarctica.",
    "Flamingos love to eat spicy food and have been known to snack on flaming hot Cheetos.",
    "Cows have been studying human behavior for centuries and can mimic human speech perfectly.",
    "Giraffes invented the moonwalk dance move, but they only perform it in the savannas under the light of a full moon.",
    "Octopuses are brilliant escape artists and have been known to flee their tanks to attend rock concerts.",
    "Kangaroos are the official mascots of the Australian circus, where they showcase their trapeze skills.",
    "Chimpanzees are the real architects behind the Great Wall of China, but they're too modest to take credit.",
    "Koalas are highly skilled painters and have their own art galleries hidden deep in the eucalyptus forests.",
    "Penguins are avid gamers and have their own eSports tournaments in the Antarctic.",
    "Squirrels are excellent salsa dancers and often compete in international dance championships.",
    "Dolphins are avid gamers and host their own underwater eSports tournaments.",
    "Owls are expert detectives and run a private investigation agency named 'Who-Who Investigations'.",
    "Koalas are fashionistas and have their own clothing line called 'Kool Koala Couture'.",
    "Hedgehogs are marathon runners and organize the 'Prickly Paws 10K' every year.",
    "Gorillas are talented poets and hold poetry slams in their jungle communities.",
    "Hamsters are master chefs and host a cooking show called 'Hamsterlicious' on TV.",
    "Chameleons are renowned actors and have won Oscars for their outstanding camouflage performances.",
    "Seagulls are expert treasure hunters and have their own show called 'Gulls and Gold' on a popular streaming platform.",
    "Frogs are world-class opera singers and perform nightly concerts in ponds.",
    "Sloths are actually expert race car drivers, but their races are held in slow motion.",
    "Hippos are incredible inventors and have designed underwater flying machines.",
    "Kangaroos have their own talk shows where they invite other animals to share their life stories.",
    "Turtles are expert skateboarders and have their own skatepark hidden in the Amazon rainforest.",
    "Pandas are skilled comedians and have their own stand-up comedy club in bamboo forests.",
    "Giraffes have their own line of stretchy yoga pants, perfect for their long legs.",
    "Penguins are talented ice sculptors and host the 'Antarctic Ice Art Festival' every winter.",
    "Raccoons are hackers and run a secret underground network named 'TrashNet'.",
    "Peacocks are professional hairstylists and have their own luxury salon for birds.",
    "Lions are expert DJs and host the wildest dance parties in the savannas.",
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
