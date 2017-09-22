# Function to generate (k,k*k)
def genDict(sr):
    series = dict()
    for en in range(1, int(sr) + 1):
        series[en] = en * en
    print(series)


print("********Generate (k,k*k) dictionary********** \n")
sr = input("Enter the series to be generated: ")
genDict(sr)
