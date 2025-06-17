while True:
    user_input = input ("Say something (Type'STOP' to exit): ")

    if user_input.upper() == "STOP":
        print("Stoping the program.")
        break

    print(f"I got that: {user_input}")
    