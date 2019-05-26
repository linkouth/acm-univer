import collections

def get_first_lower_than(dict, num):
    for key in dict:
        if key < num and dict[key] > 0:
            dict[key] = dict[key] - 1
            return key
    for key in dict:
        if key > num and dict[key] > 0:
            dict[key] = dict[key] - 1
            return key

def get_not_null_key(dict):
    for key in dict:
        if dict[key] != 0:
            return key

if __name__ == '__main__':
    number = int(input('Enter the number: '))
    # number = 7685638
    dict = collections.Counter()
    for char in sorted(list(str(number))):
        dict[char] += 1
    anagramm = ''
    i = 0
    for char in str(number):
        tmp = get_first_lower_than(dict, char)
        if str(number)[i] != tmp and tmp != None:
            anagramm += tmp
        else:
            tmp = get_not_null_key(dict)
            j = i
            while j > 0 and str(number)[j] == tmp and tmp <= anagramm[j - 1]:
                j -= 1
            print(j)
            # if str(number)[i] != anagramm[j]:
            anagramm = anagramm[:j - 1] + tmp + anagramm[j - 1:len(anagramm)]
        i += 1
    print(anagramm)
