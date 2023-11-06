def main(string):
    pass1 = 0
    pass2 = 0
    pass3 = 0
    
    if string[0].isalpha():
        if len(string) >=  4:
            for ctr in string:
                if ctr.isupper():
                    pass1 +=1
                elif ctr.isdigit():
                    pass2 +=1
                elif ctr != '/' and ctr != ' ':
                    pass3 +=1
    if pass1 >= 1 and pass2 >= 1 and pass3 >= 1:
        return 1
    else:
        return 0

string = input()
print(main(string))