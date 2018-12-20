import os
import sys

# this program will feed the API while API is running on http://localhost:5000

# parameter: company name. ex. apple
in_search = sys.argv[1]


print('executing search for {} script on LinkedIn:'.format(in_search))
exes = ['curl -i http://localhost:5000/todo/api/v1.0/tasks/' + in_search]

ex_command = ' '.join(exes)

# executes the command
os.system(ex_command)
