def reverse_function(data_list):
    length = len(data_list)
    s = length
    new_list = [None]*length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    return (new_list)

reverse_function([1,3,5,0,8,1])
