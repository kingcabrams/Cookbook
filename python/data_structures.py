courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
nums = [1, 5, 2, 4, 3]


def main():
    """Lists"""
    courses.append('Art')
    print(courses)
    popped = courses.pop()  # Pop by default removes last value

    courses.insert(0, 'Art')
    print(courses)
    courses.remove('Art')  # Removes first instance of 'Art' in the list

    courses.extend(courses_2)
    print(courses)

    courses.reverse()
    print(courses)

    courses.sort()
    nums.sort()
    print(courses)
    print(nums)

    nums.sort(reverse=True)
    print(nums)

    print(max(nums))
    print(sum(nums))

    print(courses.index('CompSci'))  # Prints index of first occurrence
    for index, course in enumerate(courses, start=1):
        print(index, course)

    course_str = ', '.join(courses)  # List to string

    new_list = course_str.split(', ')

    print(course_str)
    print(new_list)

    # Sublists with Slices
    print(courses[0:2])
    print(courses[:2])  # Assumes first value as first index
    print(courses[1:])  # Assumes second value as last index

    # Downside of mutable objects
    new_list2 = new_list

    new_list2[0] = 'English'  # Changes both lists

    print(new_list2)
    print(new_list)

    # Empty Lists
    empty_list = []
    empty_list = list()

    """Tuples"""
    tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
    tuple_2 = tuple_1

    print(tuple_1)
    print(tuple_2)

    # tuple_1[0] = 'Art'  # Can't modify tuple it is immutable

    # Empty Tuples
    empty_tuple = ()
    empty_tuple = tuple()

    """Sets"""
    cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
    art_courses = {'History', 'Math', 'Art', 'Design'}

    print(cs_courses)  # Order doesn't matter in sets

    print(cs_courses.intersection(art_courses))
    print(cs_courses.difference(art_courses))
    print(cs_courses.union(art_courses))

    # Empty Sets
    empty_set = {}  # This isn't right! This is an empty dictionary
    empty_set = set()

    """Dictionaries"""


main()
