def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    total_words = len(words)
    
    print(f"Total number of words: {total_words}")

if __name__ == "__main__":
    main()