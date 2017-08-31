# Word Count Program

# Read input from a file
inputFile = open("sampleIP.txt", "r+")

# Write output to a file
outputFile = open("sampleOP.txt", "w+")

# Count array declare
count = {}

# Loop and split each word in the file
for word in inputFile.read().split():
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

# Output the word and count to a file
for w, c in count.items():
    outputFile.write(w)
    outputFile.write(":\t")
    outputFile.write(str(c))
    outputFile.write("\n")
print("Done! Please Check sampleOP.txt")

# Close files
inputFile.close()
outputFile.close()
