# Pangram Check Program

# Function to check for Pangram with input as string
def checkAlphabetsInString(s):

    # List declare
    list = []
    numOfAlphabets = 26

    # List instantiate and set all 26 alphabets to false
    for a in range(numOfAlphabets):
        list.append(False)

    # Change words to lower case and iterate
    for w in s.lower():
        if not w == " ":
            # Set to true
            list[ord(w) - ord('a')] = True

    # Return false if an alphabet is missing, true otherwise
    for alp in list:
        if not alp:
            return False
    return True

# Input String
line=input("Enter the sentence\n")
# Example for perfect pangram - "Jaded zombies acted quaintly but kept driving their oxen forward"
print(checkAlphabetsInString(line))