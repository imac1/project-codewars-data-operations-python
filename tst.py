import itertools
# txt = "abc1d2"
# # numbers = []
# # for i in range(len(txt)):
# #     if txt[i].isnumeric():
# #         numbers.append(txt[i])

# # for i in numbers:
# #     print(i)

# x = int(''.join(filter(str.isdigit, txt)))
# print(x)

# ! TODO de refacut
# lst = [1, 19, 6, 2, 12, -3]

# res = []
# for el in range(len(lst)):
#     if el % 2 != 0:
#         res.append(lst[el]*2)
#     else:
#         res.append(lst[el])

# print(res)

# li = {'Ice': 'Cream', 'Age': '21', 'Light': 'Cream', 'Double': 'Cream'}
# empty_flip = {}
# for key, value in li.items():
#     if value not in empty_flip:
#         empty_flip[value] = [key]
#     else:
#         empty_flip[value].append(key)
# print(empty_flip)


# TODO !! flatten operations !!

regular_list = [1, [1, 1]]
# flat_list = list(itertools.chain(*regular_list))
# print(flat_list)
# print(sum(flat_list))
# flat = []
# for elem in regular_list:
#     if type(elem) is list:
#         for item in elem:
#             flat.append(item)
#     else:
#         flat.append(elem)
# print(flat)

# TODO nesting depth
# 1
def maxdepth(tree):
    if isleaf(tree):
        return 1
    maximum = 0
    for child in children(tree):
        depth = maxdepth(child)
        if depth > maximum:
            maximum = depth
    return maximum + 1
# 2
# temp=list(filter(lambda x:x in ('[',']'), str(l)))
# while temp[-1]==']':
#     temp.pop()
# return temp.count('[')-temp.count(']')

# 3
def list_depth(l):
    m=0
    ls=[]
    for i in str(l):
        if i=='[':
            m+=1
        elif i==']':
            ls.append(m)
            m-=1
    return max(ls) 
