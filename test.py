try:
    term = input("Type something: ")
    if not term:
        raise ValueError("Empty input!")
except ValueError as e:
    print("ERROR:", e)