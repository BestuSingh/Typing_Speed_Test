import time

def calculate_typing_speed(text, time_taken):
    words = len(text.split())
    typing_speed = words / (time_taken / 60)
    return typing_speed

def typing_speed_test():
    print("Welcome to the Typing Speed Test")
    print("Type the following text as fast as you can!")
    print("-----------------------------------------------")
    text = "Remember that wherever your heart is, there you will find your treasure."
    print(text)
    print("-----------------------------------------------")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    time_taken = end_time - start_time 
    typing_speed = calculate_typing_speed(text, time_taken)
    print("-----------------------------------------------")
    print("Time taken: ", round (time_taken, 2), "seconds")
    print("Typing speed: ", round(typing_speed, 2), "words per minute")
    
typing_speed_test()
