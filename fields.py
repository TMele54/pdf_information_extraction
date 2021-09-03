import re

s = "abc123AUG|GAC|UGAasdfg789"
pattern = "AUG\|(.*?)\|UGA"

substring = re.search(pattern, s).group(1)
print(substring)
OUTPUT