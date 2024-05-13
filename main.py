def main():
    text = getBookContent("books/frankenstein.txt")
    print(text)
    print(count_words(text))
    counts = count_letters(text)
    print(counts)

def getBookContent(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    counts = {}
    for i in range(ord('a'),ord('z')):
        counts[chr(i)] = text.count(chr(i))
    return counts
    
main()