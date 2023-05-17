import sys
import Levenshtein

if len(sys.argv) != 3:
    print("⚠️ Please provide two strings as command-line arguments.")
    sys.exit(1)

string1 = sys.argv[1]
string2 = sys.argv[2]

distance = Levenshtein.distance(string1, string2)
print(distance)

