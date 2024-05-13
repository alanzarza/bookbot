def main():
    path = "books/frankenstein.txt"
    text = getBookContent(path)
    word_count = count_words(text)
    counts = count_letters(text)

    print(f"---Begin report of {path} ---")
    print(f"{word_count} words found in document")

    list = count_letters(text)

    reverse(list)

    for i in list:
        print(f"The '{i["name"]}' character was found {i["num"]} times")
        
    print("--- End Report ---")


def getBookContent(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    count_list = []
    for i in range(ord('a'),ord('z')+1):
        counts = {
            "name":chr(i),
            "num":text.count(chr(i))
        }
        count_list.append(counts)
    return count_list

def sort_on(dic):
    return dic["num"]

def reverse(list):
    list.sort(reverse=True,key=sort_on)
    
main()