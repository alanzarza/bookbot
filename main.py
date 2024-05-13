def main():
    text = getBookContent("books/frankenstein.txt")
    print(text)
    print(count_words(text))

def getBookContent(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)
    
main()