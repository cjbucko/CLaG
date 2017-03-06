# Challenge Level: Intermediate and Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially because you're putting them up on GitHub!

# For the purposes of this exercise, we're going to use unrealistically perfect and uniform addresses, and one-word first names :)

studybuddy_1 = 'Alison McCauley, 1234 County Line Road, Skaneateles, NY 13152'
studybuddy_2 = 'Dee Cater, 555 Bradford Pkwy, Syracuse, NY 13224'
studybuddy_3 = 'Andrea Bianchi, 987 South St, Jamesville, NY 13078'
studybuddy_4 = 'Kristen Link Logan, 264 Craig Street, Syracuse, NY 13211'
studybuddy_5 = 'Nina Verity, 111 Bridge St, Solvey, NY 13209'

# Goal 1: Create a program that simply shows all the ZIP codes.
# Sample output:
# 13152
# 13224
# 13078
# (etc)

# Goal 2: Modify your program to output all the ZIP codes on the same line, with an an explanatory sentence.
# Sample output: (but use any language you want!)
# Our study group included people from these ZIP codes: 13152, 13224, 13078, (etc).

# Goal 3: Modify your program to show each study buddy's first name and ZIP code.
# Sample output: (again, use any language you want!)
# Alison lives in 13152.
# Dee lives in 13224.
# Andrea lives in 13078.
# (etc)

print ("{0}\n{1}\n{2}\n{3}\n{4}\n".format(studybuddy_1[-5:], studybuddy_2[-5:], studybuddy_3[-5:], studybuddy_4[-5:], studybuddy_5[-5:]))

print ("Our class includes people from the following zip codes: {0}, {1}, {2}, {3}, {4}.\n".format(studybuddy_1[-5:], studybuddy_2[-5:], studybuddy_3[-5:], studybuddy_4[-5:], studybuddy_5[-5:]))

first_name1 = studybuddy_1.split()[0]
print (first_name1)

first_name2 = studybuddy_2.split()[0]
print (first_name2)

first_name3 = studybuddy_3.split()[0]
print (first_name3)

first_name4 = studybuddy_4.split()[0]
print (first_name4)

first_name5 = studybuddy_5.split()[0]
print (first_name5)

print ("""\n{0} lives in zip code {1}\n{2} lives in zip code {3}\n{4} lives in zip code {5}\n{6} lives in zip code {7}\n{8} lives in zip code {9}""".format
       (first_name1, studybuddy_1[-5:], first_name2, studybuddy_2[-5:], first_name3, studybuddy_3[-5:], first_name4, studybuddy_4[-5:], first_name5, studybuddy_5[-5:]))


