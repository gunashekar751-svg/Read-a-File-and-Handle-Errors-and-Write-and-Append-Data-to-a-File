try:
    with open("sample.txt", "rt") as file:
        print("Reading file content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(" The file 'sample.txt' was not found.")

