def add(num_list):
    result = num_list[0]
    for n in num_list[1:]:
        result += n
    return result

def sub(num_list):
    result = num_list[0]
    for n in num_list[1:]:
        result -= n
    return result
