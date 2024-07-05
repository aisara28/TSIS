import re

def match_ab(string):
    pattern = r'^a+b*$'
    if re.search(pattern, string):
        return True
    else:
        return False


print(match_ab("ab"))      
print(match_ab("abb"))     
print(match_ab("abbb"))  
print(match_ab("a"))      
print(match_ab("ac"))     
print(match_ab("b"))      

    
