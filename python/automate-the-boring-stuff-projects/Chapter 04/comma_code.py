def list_to_string(spam):
    string_of_list = ''
    for i in range(len(spam)):
        if i == len(spam) - 1:
            string_of_list += 'and ' + spam[i]
        else:
            string_of_list += spam[i] + ', '
    print(string_of_list)
    return string_of_list


def main():
    example_list = ['apples', 'bananas', 'tofu', 'cats']
    list_to_string(example_list)


main()
