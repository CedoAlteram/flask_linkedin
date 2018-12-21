import os
import sys
import re

# this program will feed the API while API is running on http://localhost:5000

import re


def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s


# parameter: company name. ex. apple, people data labs
in_search = sys.argv[1]

url_in_search = urlify(in_search)

print('executing search for {0} script on LinkedIn:'.format(url_in_search))
exes = ['curl -i http://localhost:5000/todo/api/v1.0/tasks/' + url_in_search]

print(exes)
ex_command = ' '.join(exes)

# executes the command
os.system(ex_command)
