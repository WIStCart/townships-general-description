"""
Convert text file to JSON format for use in webapp.

Author: Hayden Elza
Email: hayden.elza@gmail.com
Created: 2019-07-26
"""


import os
import re
import json


# Set file paths
wd = os.path.dirname(os.getcwd())
in_file = os.path.join(wd, 'data/edited/township_descriptions.txt')
out_file = os.path.join(wd, 'data/edited/township_descriptions.json')

# Define dict
desc_dict = dict()

# Read in_file
with open(in_file) as infile:

	# For each line
	for line in infile:

		# If new DTR is found write current record to dict, then start new record
		if re.search(r'((?<=[\r\n])|^|(?<=[\r\n] {1}))T[0-9]{1,2}NR[0-9]{1,2}[WE]([\r\n]|(?= [\r\n]))', line):
			
			try: 
				township = record.split('\n', 1)[0]

				d = '2' if township[-1] == 'W' else '4'
				t = re.search(r'(?<=T)[0-9]{1,2}', township).group().zfill(2)
				r = re.search(r'(?<=NR)[0-9]{1,2}', township).group().zfill(2)
				dtr = d + t + r

				desc = record.split('\n', 1)[1]

				# Remove characters
				expressions = [
					["[\n\r\t]"," "],
					[" {2,}"," "],
					["((^ )|( $))",""],
					["\*{2,}(?=[^\*\r\n]+)","Notes from Digitizer: "],
					["\*{2,}",""],
					["(?<=\w) -(?=\w)",""],
					["(?<=\w)- (?=\w)",""]
				]
				for expression in expressions: 
					desc = re.sub(expression[0], expression[1], desc)
				
				# Add to dict
				desc_dict[dtr] = desc

			# First line will throw error because record is not defined, ignore
			except NameError: pass

			# Start new record with DTR that was found
			record = line
		
		# If no new DTR is found, add line to record
		else: record+=line

# Write dict to json file
with open(out_file, 'w') as f:
	json.dump(desc_dict, f)