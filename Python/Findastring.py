def count_substring(string, sub_string):
    #return count_helper(string, sub_string, 0)
    return sum([1 for i in range(len(string)) if string[i:].find(sub_string) == 0])

def count_helper(string, sub_string, count):
    found_index = string.find(sub_string)
    if  found_index != -1:
        return count_helper(string[found_index+1:], sub_string, count+1)
    else:
        return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)