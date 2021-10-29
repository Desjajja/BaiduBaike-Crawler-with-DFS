#-------------------------------------------------------------------------------------------------#
#	General Configrations
#-------------------------------------------------------------------------------------------------#
from enum import Flag, auto


MAX_DEPTH = 2		# maximum depth of DFS trees
FILE_TYPE = 'csv'	# output file type [csv, txt]

class genre(Flag):
	failed = 0
	succeeded = auto()
# 1 represents result, 0 represents failure