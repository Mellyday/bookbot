def sort_on(dict):
    return dict['num']

def print_report(text):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(text.split())} words found in the document')
    print()
    charlist = count_char(text)
    characters = []
    for entry in charlist:
        characters.append({"name": entry, "num": charlist[entry]})
    characters.sort(reverse=True, key=sort_on)
    for ch in characters:
        print(f"The '{ch['name']}' character was found {ch['num']} times")
    print('--- End report ---')

def count_char(text):
    text = text.lower()
    result = {}
    for ch in text:
        if ch not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        if ch not in result.keys():
            result[ch] = 1
        else:
            result[ch] += 1
    return result

with open('books/frankenstein.txt') as f:
    text = f.read()
    print_report(text)

