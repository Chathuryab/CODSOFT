#PASSWORD GENERATOR
import string
import random
if __name__=="__main__":
    #TO INCLUDE ALL CHARACTERS
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation
    #PROMPTING USER TO MENTION LENGHT OF PASSWORD
    plen=int(input("enter password lenght\n"))
    s=[]
    # ADDING ALL OUR CHARACTERS IN THIS STRING
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # USED TO GIVE RANDOMLY PASSWORDS
    random.shuffle(s)
    #PRINTING PASSWORD
    print("here is your password:")
    print("".join(s[0:plen]))
