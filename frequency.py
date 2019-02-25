import re

def split_text(string_iterable):
    line_stream = iter(string_iterable)
    for line in line_stream:
        for word in re.split(r'\W+', line):
            yield word


if __name__ == '__main__':
    words = []
    with open('input.txt', 'r') as myself:
        for word in split_text(myself):
            words.append(word)

    d = {}
    count = 0

    for word in words:
        for letter in word:
            d[letter] = d.get(letter, 0) + 1
            count += 1

    sorted_by_value = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    for key, value in sorted_by_value:
        f = open("output.txt", "a")
        f.write('{0:s}: {1:.3f}\n'.format(key, value / count))
