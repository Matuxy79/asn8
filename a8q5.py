#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

def MothraCount(a, b):
    if a == 1 or b == 1:
        return 1
    elif a == 2 and b == 2:
        return 2
    else:
        return MothraCount(a-1, b) + MothraCount(a, b-1)

#part B
print(MothraCount(3, 3))   # Output: 6
print(MothraCount(4, 4))   # Output: 20
print(MothraCount(10, 12)) # Output: 4457400
