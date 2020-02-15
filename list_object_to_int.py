
def list_object_sum(str1):
    # A temporary str1ing
    temp = " "
    # holds sum of all numbers
    # present in the str1ing
    sm = 0
    # read each character in input string
    for ch in str1:
        # if current character is a digit
        if ch.isdigit():
            temp += ch
        # if current character is an alphabet
        else:
            # increment Sum by number found
            # earlier(if any)
            sm += int(temp)
            # reset temporary str1ing to empty
            temp = "0"
    # atoi(temp.c_str1()) takes care
    # of trailing numbers
    return sm + int(temp)