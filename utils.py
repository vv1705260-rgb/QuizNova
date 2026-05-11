import os
import time

# Clear Console
def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")

# Loading Animation
def loading_animation():

    print("\n⏳ Loading Quiz", end="")

    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.4)

    print("\n")
