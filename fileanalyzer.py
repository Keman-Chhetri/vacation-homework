def analyze_file():
    try:
        file_name = input("Please enter the name of the text file: ")
        with open(file_name, 'r') as file:
            content = file.read()

        words = content.split()
        lines = content.count('\n') + 1
        characters = len(content)

        print(f"Total words: {len(words)}")
        print(f"Total lines: {lines}")
        print(f"Total characters: {characters}")

        

    except FileNotFoundError:
        print("The file was not found.")

analyze_file()

       