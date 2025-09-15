import threading
import time


def take_order():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(2) # simulating that on the OS we're having some other task being performed! like a db call
        # or a file reading operation etc...

def brew_chai():
    for i in range(1,4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)



# Creating thread...

order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()

