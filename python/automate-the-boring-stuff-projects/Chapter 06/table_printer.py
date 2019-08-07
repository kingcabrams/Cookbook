"""Prints a nicely aligned table from a list of strings."""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def print_table(table):
    col_widths = []
    for item_list in table:
        max_length = 0
        for item in item_list:
            item_length = len(item)
            if item_length > max_length:
                max_length = item_length
            if item == item_list[-1]:
                col_widths.append(max_length)

    # Iterates over lists taking nth element from each
    # and printing it with the other nth subitems
    # right aligned according to the corresponding col_width value

    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].rjust(col_widths[item]), end=' ')
        print()


print_table(table_data)


