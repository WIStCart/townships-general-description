"""
Merge files that are devided out by range number into a single file.

Author: Hayden Elza
Email: hayden.elza@gmail.com
Created: 2019-07-26
"""


import os


# Data Sources
wd = os.path.dirname(os.getcwd())
west = os.path.join(wd, 'data/edited/TownshipsWest/')
east = os.path.join(wd, 'data/edited/TownshipsEast/')
sources = [west,east]

output = os.path.join(wd, 'data/edited/township_descriptions.txt')

# Open output
with open(output, 'w') as outfile:

	# Iterate through sources
	for source in sources:

		# Walk directory
		for dir_name, subdirs, files in os.walk(source):
			print('Found directory: %s' % dir_name)

			# Read each line for each file and write to output file
			for file in files:
				print('\t%s' % file)
				with open(os.path.join(dir_name, file)) as infile:
					for line in infile:
						outfile.write(line)
