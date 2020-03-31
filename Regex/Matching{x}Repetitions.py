Regex_Pattern = r'^[a-zA-z02468]{40}[13579\W]{5}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())