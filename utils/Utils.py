def ReverseTuples(tuples):
    new_tup = tuples[::-1]
    return new_tup

 
def Camelcase2Split(str):
    words = [[str[0]]]
 
    for c in str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)
    return ' '.join([''.join(word) for word in words])

# Hack: string type that is always equal in not equal comparisons
class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False
# Our any instance wants to be a wildcard string
any = AnyType("*")
