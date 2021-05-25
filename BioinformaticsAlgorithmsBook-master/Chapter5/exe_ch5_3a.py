from re import search

def find_prosite(seq, profile):
    regexp = profile.replace("−", "")
    regexp = regexp.replace("x", ".")
    regexp = regexp.replace("(", "{")
    regexp = regexp.replace(")", "}")
    mo = search(regexp, seq)
    if (mo != None):
        return mo.span()[0]
    else:
        return -1

def test():
    seq = "HKMMLASCKHLLCYLKFY"
    print(find_prosite(seq, "Y−x−x−F−[YT]"))

test()