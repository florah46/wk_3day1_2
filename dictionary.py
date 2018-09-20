def make_dictionary(lower, upper):
    my_dic = {}

    for x in range(lower,upper):
        my_dic[x] = x*x
    return my_dic       
print(make_dictionary(1,16))