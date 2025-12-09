def main():
    input("Press Enter to start the app...")
    # Just to be able to see all the logs
    
    print("Welcome to the interactive Python container!")
    name = input("What's your name? ")
    print(f"Nice to meet you, {name}!")

    while True:
        cmd = input("Type something (or 'exit' to quit): ")
        if cmd.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        print(f"You said: {cmd}")

if __name__ == "__main__":
    main()