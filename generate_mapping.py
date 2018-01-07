"""
This script will load in the CR and generate a mapping to a sane rules label,
so that we may consistently and automatically tag questions. 
This is not intended to preclude the addition of other, human-generated tags.
It uses the CSV version of the CR, for example:
http://media.wizards.com/2017/downloads/MagicCompRules%2020170925.txt
LEF 2018 01 07
"""

import os
import re
import sys
import codecs

path_to_csv = '/home/louisf/Dropbox/mtg/mtg_rules_mapping/data/MagicCompRules 20170925.txt'

with open(path_to_csv, 'r', encoding='windows-1252') as f:
    print(f.readlines())

