import sys

# Đếm từ
def print_words(filename):
    words_count = readfile_count_words(filename)
    words_count_sorted =  sorted(list(words_count), key = lambda k: k[0])
    for i in words_count_sorted:
        print (i, ":", words_count[i])

def print_top(filename):
    words_count = readfile_count_words(filename)
    words_count_sorted =  sorted(list(words_count), key = words_count.get, reverse = True)
    l = len(words_count_sorted)
    for i in range(20):
        if i < l:
            print (words_count_sorted[i], ":", words_count[words_count_sorted[i]])

def readfile_count_words(filename):
    f =  open(filename, encoding='utf-8-sig')
    content = remove_special_char(f.read())
    list_str = content.split(" ")
    dict_count = {}
    for i in list_str:
        if i == '': continue
        i = i.lower()
        if i in dict_count: dict_count[i] += 1
        else: dict_count[i] = 1

    return dict_count
def remove_special_char(str):
    special_char = ['.', ',', '?', '!', '\n', '\r', '(', ')', '[', ']', ':', '--', ';', '`', "' ", '"']
    for j in special_char:
        str = str.replace(j, " ")
    return str
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()