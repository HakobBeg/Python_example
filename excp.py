fruits = {"banana": 15, "apple": 65, "pear": 0}

while True:
    try:
        key = input("Enter fruit name: ")

        print(fruits[key])

        if fruits[key] <= 0:
            raise Exception(f"There's no {key} left in the box.")
    except KeyError:
        print(f"There's no such fruit as {key}, sorry.")
    except Exception as ex:
        print(ex)
    except KeyboardInterrupt:
        print("Goodbye")
        exit()

print("qwer")
