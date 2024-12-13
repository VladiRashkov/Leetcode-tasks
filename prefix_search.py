def prefix_search(collection):
    prefix = ''
    count = 0
    for i in range(len(collection)-1):
        if i == 0:
            for element in collection[i]:
                if count == 2:
                    break
                prefix += element
                count+=1
        else:
            if prefix in collection[i]:
                continue
            else:
                return ''

    return prefix


strs = ["flower", "flow", "flight"]

print(prefix_search(strs))
