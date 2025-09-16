import asyncio
import time

async def make_tea():
    print("Making Tea...")
    await asyncio.sleep(2) # mimicing that this will come after 2 seconds... (this is asynchronous) 
    # As soon as eventloop sees that it will reqquire sometime so it will immediately execute next task in the queue.
    # Here the next task is immidiately awoken that is make_snacks...
    # time.sleep(2)
    print("Tea Ready!...")

async def make_snacks():
    print("Preparing Snacks...")
    await asyncio.sleep(2) 
    # time.sleep(2)
    print("Snacks Ready!...")

async def main():
    start = time.time()
    await asyncio.gather(
        make_tea(),
        make_snacks()
    )
    end = time.time()
    print(f"Total time required: {end-start:.2f} seconds")

asyncio.run(main()) # starts the event-loop...