"""Program that makes a mad libs"""

mad_libs = open(input("Enter the name of the .txt file you would like to use: "))
mad_libs_answers = open('mad_libs_answers.txt', 'w')

line = mad_libs.read().split()

for i in range(len(line)):
    if line[i] == 'ADJECTIVE':
        line[i] = input("Enter an adjective: ")
    elif line[i] == 'NOUN':
        line[i] = input("Enter a noun: ")
    elif line[i] == 'ADVERB':
        line[i] = input("Enter an adverb: ")
    elif line[i] == 'VERB':
        line[i] = input("Enter a verb: ")

story = ' '.join(line)
print(story)
mad_libs_answers.write(story)



