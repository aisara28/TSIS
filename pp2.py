#1
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

#2
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

#3
import re

def find_lowercase_underscore(string):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, string)


print(find_lowercase_underscore("hello_world and foo_bar"))

#4
import re

def find_uppercase_lowercase(string):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, string)


print(find_uppercase_lowercase("HelloWorld and CamelCaseString"))

#5
import re

def match_a_anything_b(string):
    pattern = r'^a.*b$'
    if re.search(pattern, string):
        return True
    else:
        return False


print(match_a_anything_b("acb"))     
print(match_a_anything_b("afoobarb")) 
print(match_a_anything_b("ab"))      
print(match_a_anything_b("axxxb")) 

#6
import re

def replace_space_comma_dot(string):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', string)


print(replace_space_comma_dot("Hello, world. How are you?"))

#7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


print(snake_to_camel("hello_world")) 
print(snake_to_camel("this_is_snake_case")) 

#8
import re

def split_at_uppercase(string):
    return re.findall('[A-Z][^A-Z]*', string)


print(split_at_uppercase("HelloWorld")) 
print(split_at_uppercase("CamelCaseString"))

#9
import re

def insert_spaces_capital(string):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', string)


print(insert_spaces_capital("HelloWorld"))  
print(insert_spaces_capital("CamelCaseString"))
    
#10
import re

def camel_to_snake(camel_str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camel_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


print(camel_to_snake("HelloWorld")) 
print(camel_to_snake("CamelCaseString"))