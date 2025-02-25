import os
import regex as re

if os.path.exists('9 - Miscellaneous'):
    for i in os.listdir('9 - Miscellaneous'):
        match = re.match(r'\d+\s-\s(.*)', i) 
        if match: 
            new_name = match.group(1)
            os.rename('9 - Miscellaneous/' + i, '9 - Miscellaneous/' + new_name)