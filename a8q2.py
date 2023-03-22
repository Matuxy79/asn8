#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#part A
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#part B
def moosonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return n - 1
    else:
        return moosonacci(n-1) + moosonacci(n-2) + moosonacci(n-3)

#part C
def substr(s, c, r):
    if not s:  # base case: empty string
        return ""
    elif s[0] == c:  # target found at beginning of string
        return r + substr(s[1:], c, r)
    else:  # target not found at beginning of string
        return s[0] + substr(s[1:], c, r)
