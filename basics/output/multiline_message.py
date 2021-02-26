#Display message to standard output in multiple lines of code

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f" System reboot started at {time.strftime('%X')}")
    await say_after(1, ' ')
    await say_after(1, '...rebooting sensory system')
    await say_after(2, '...rebooting output motors')
    await say_after(3, '...rebooting hover engine\n')
    await say_after(3, ' ')
    

    print(f"Reboot succesfuly at {time.strftime('%X')}")


    await say_after(1, ' ')
    await say_after(2, 'All systems are ONLINE')

asyncio.run(main())