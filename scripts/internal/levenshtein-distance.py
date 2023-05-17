import sys
import Levenshtein

if len(sys.argv) != 3:
    print("⚠️ Please provide two strings as command-line arguments.")
    sys.exit(1)

string1 = sys.argv[1]
string2 = sys.argv[2]

# determine if string1 or string2 fully contains the other and if so print(0) to emulate a match
if string1 in string2 or string2 in string1:
    print(0)
    sys.exit(0)
distance = Levenshtein.distance(string1, string2)
print(distance)

