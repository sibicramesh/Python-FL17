# Function to remove duplicates and sort them
def removeDuplicates(inp):
    terms = set()
    result = ''

    for ew in inp.split():
        if ew not in terms:
            result = result + ew + ' '
            terms.add(ew)
    result = sorted(terms)
    print(' '.join(result))


print("********Removing Duplicates and Sorting********** \n")
inp = input("Enter String: ")
removeDuplicates(inp)