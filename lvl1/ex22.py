# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. I have a .txt file for you, if you want to use it!

# Extra:

#     Instead of using the .txt file from above (or instead of, if you want the challenge), take this .txt file, and count how many of each “category” of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you’re going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

def main():
    names = {}
    with open("names.txt", 'r') as of:
        line = of.readline()
        while line:
            line = line.strip()
            names[line] = names.get(line) + 1 if names.get(line) else 1
            line = of.readline()

    print(names)

def extra():
    categories = {}
    with open("files.txt", 'r') as of:
        line = of.readline()
        while line:
            line = line[3: -26]
            categories[line] = categories.get(line) + 1 if categories.get(line) else 1
            line = of.readline()

    print(categories)

if __name__ == "__main__":
    main()
    extra()