import re

def match_ab_range(string):
    pattern = r'^ab{2,3}$'
    if re.search(pattern, string):
        return True
    else:
        return False


print(match_ab_range("abb"))    
print(match_ab_range("abbb"))   
print(match_ab_range("ab"))     
print(match_ab_range("abbbb"))  
print(match_ab_range("acb"))    
                       






    




    
    

    
    




    

    


   

 