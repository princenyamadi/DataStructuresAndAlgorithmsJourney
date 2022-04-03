from re import S


command = ""
started = False

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
        print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            print("Car stopped...")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("Sorry, I don't understand that command")
