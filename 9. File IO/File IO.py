
# 1 Write a program to create a new text file and write 'Hello, Python!' into it.
with open("hello_python.txt", "w") as file:
    file.write("Hello, Python!")


# 2 Read the content of a file and print it line by line.
with open("hello_python.txt", "r") as file:
    for line in file:
        print(line.strip())
        
        
# 3 Write a list of names into a file (one name per line).
names = ["Alice", "Bob", "Charlie"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
        

# 4 Append new data to an existing file.
with open("names.txt", "a") as file:
    file.write("David\n")


# 5 Count how many lines, words, and characters are in a text file.
with open("names.txt", "r") as file:
    content = file.read()
    lines = content.splitlines()
    word_count = len(content.split())
    char_count = len(content)
    print("Lines:", len(lines))
    print("Words:", word_count)
    print("Characters:", char_count)


# 6 Copy the content of one file to another.
with open("names.txt", "r") as source_file:
    content = source_file.read()
with open("names_copy.txt", "w") as dest_file:
    dest_file.write(content)

    
# 7 Find and replace a word in a text file.
with open("names.txt", "r") as file:
    content = file.read()
    content = content.replace("Alice", "Alicia")
with open("names.txt", "w") as file:
    file.write(content)


# 8 Read numbers from a file and calculate their sum.
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
    total = sum(numbers)
    print("Total Sum:", total)


# 9 Write a program that reads a paragraph and counts how many times each word appears (word frequency counter).
with open("paragraph.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print("Word Frequency:")
    for word, count in word_count.items():
        print(f"{word}: {count}")


# 10 Read a log file and display only lines containing a specific keyword (like 'ERROR').
with open("log.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip()) 