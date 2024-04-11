def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            #print(file_contents)

            words = file_contents.split()
            word_count = 0

            for word in words:
                if word != None:
                    word_count += 1
  
            print(f"There are {word_count} words in the document.")
            return word_count
            
main()