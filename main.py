def solution(str):
    return "".join([" " + char if char.isupper() else char for char in str])

# Complete the solution so that the function will break up camel casing,
# using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""