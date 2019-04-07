def mad_max(one,two,three):
    if one>two and one>three:
        return one
    elif two> three:
        return two
    else:
        return three

print(mad_max(1,2,3))
print(mad_max(-1,-2,-3))
print(mad_max(-1,2,-3))
