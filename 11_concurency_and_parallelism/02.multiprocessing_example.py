from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai Brewing!")
    time.sleep(3)
    print(f"End of {name} chai Brewing!")


if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

# start all Process

    for p in chai_makers:
        p.start()

# Wait for all to wait...

    for p in chai_makers:
        p.join()

    print("All chai brewed")
