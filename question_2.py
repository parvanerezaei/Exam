# This is task 2
def minDelFunc(str1):
    Dellist = []  # List of removed character

    for i in range(0, len(str1) - 1):
        if str1[i] == str1[i + 1]:  # Compare each Characters adjacent to each other
            Dellist.append(str1[i])

    print(len(Dellist))


#Examples

# minDelFunc("AABAAB")
# minDelFunc("AAAA")
# minDelFunc("BBBBB")
# minDelFunc("ABABABAB")
# minDelFunc("BABABA")
# minDelFunc("AAABBB")
