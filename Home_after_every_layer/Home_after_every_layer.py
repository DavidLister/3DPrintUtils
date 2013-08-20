# "Home_after_every_layer.py"
#
# David Lister
#

# Can be called through terminal with the source filename as an argument else,
# the script will request is as an input.


# Imports
import sys

# G code that will be run after every layer change
home = '''
G28 X0
G28 Y0
'''

# Part of a string in the previous layer than indicates layer change 
layer_change = 'G1 Z'

# Check to see if script was run with arguments:
try:
    if sys.argv[1]:
        fname = sys.argv[1]

    else:
        # Filename input
        fname = raw_input('Please enter the filename with extention: ')

except:
    # Filename input
    fname = raw_input('Please enter the filename with extention: ')

# Open the file
source = list(open(fname, 'r'))

# Iterate through the file line by line
last_line = ''
output = ''
for line in source:
    # Check for a layer change
    if layer_change in last_line:
        output = output + home

    output = output + line
    
    last_line = line

# put '_home' after the file name
try:
    outName = fname[:fname.index('.')] + '_home' + fname[fname.index('.'):]
except:
    outName = fname + '_home'

# Save the new file
out = open(outName, 'w')
out.write(output)
out.close()

print 'Sucess,  file saved as "' + outName


