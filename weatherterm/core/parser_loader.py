import os
import re
import inspect

def _get_parser_list(dirname):
	files = [f.replace('.py','')
		for f in os.listdir(dirname)
		if not f.startswith('__')]

	return files

def _import_parsers(parserfiles):
	
	m = re.compile('.+parser$', re.I)

	_modules = __import__('weatherterm.parsers',