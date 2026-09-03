# Assigment 5: dict = {"a": 10, "b": {"c": {"d": 20}}, "e": 100} # write a program to print this output from this dictionary # output: {"a":10,"b.c.d": 20, "e": 100} 

def format_dict(data,parent_key='',separator="-"):
    formated_dict={}
    for key,value in data.items():
         new_key = f"{parent_key}{separator}{key}" if parent_key else key
         if isinstance(value, dict):
            formated_dict.update(format_dict(value, new_key, separator=separator))
         else:
            formated_dict[new_key] = value
    return formated_dict


nested_dict = {"a": 10, "b": {"c": {"d": 20}}, "e": 100}
result = format_dict(nested_dict)

print(result)
