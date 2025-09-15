import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} Started Brewing...")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} and the updated count is: {count}")
    print(f"{threading.current_thread().name} Finished Brewing...")

# creating threads...

thread_1 =  threading.Thread(target=brew_chai, name="Barista-1") # thread-1 
thread_2 = threading.Thread(target=brew_chai, name="Barista-2")  # thread-2

# Measuring the time it takes for threads to complete a task...
start = time.time()
thread_1.start() 
thread_2.start()
thread_1.join()
thread_2.join()
end = time.time()
print(f"Total time (sequential): {end-start:.2f} seconds")
    






# download_video()
# decode_video()
# listen_user_input()



# download_thread = threading.Thread(target=download_video)
# decode_thread = threading.Thread(target=decode_video)
# listen_user_input_thread = threading.Thread(target=listen_user_input)

# download_thread.start()
# decode_thread.start()
# listen_user_input_thread.start()

# download_thread.join()
# decode_thread.join()
# listen_user_input_thread.join()


