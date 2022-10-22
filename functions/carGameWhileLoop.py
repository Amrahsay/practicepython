command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            stopped = False
            print("Car started...")
    elif command == "stop":
        if stopped:
            print("Car is already stopped")
        else:
            stopped = True
            started = False
            print("Car stopped.")
    elif command == "help":
        print('''Commands available:-
[1] start - to start the car
[2] stop  - to stop the car
[3] quit  - to quit''')
    elif command == "quit":
        break
    else:
        print("Use 'help' command!")
print("_"*10)