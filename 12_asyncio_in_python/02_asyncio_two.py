import asyncio
import time


async def brew_chai(name):
    print(f"Brewing {name}")
    await asyncio.sleep(2)
    # time.sleep(2)
    print(f"{name} is ready")




async def main():
    # we use gather() to call multiple async functions...
    await asyncio.gather(
        brew_chai("Masala Chai"),
        brew_chai("Elaichi Chai"),
        brew_chai("Ginger Chai"),
    )
asyncio.run(main())