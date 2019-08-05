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

    print(courses[0:2])
    print(courses[:2])  # Assumes first value as first index
    print(courses[1:])  # Assumes second value as last index


main()
