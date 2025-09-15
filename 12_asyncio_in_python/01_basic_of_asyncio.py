# This file will hold all the knowledge about asyncio in python....
# Well till now we saw that to make our processing faster we used multi-threading as well as Parallelism.
# But without even using these both your code can be still faster and scalable.
# Yess!... just like the node.js has event loop, by using asyncio it provides you an event loop.
# You get an inbuilt library known as asyncio to perform these async tasks...


# await - Keep doing the work, I'm waiting here till you get back to me!...

import asyncio

async def brew_chai():
    print("Brewing Chai...")
    await asyncio.sleep(2)
    print("Chai is ready")


asyncio.run(brew_chai())

