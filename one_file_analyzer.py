'''
Class useful for supporting scripts that receive as input one file and 
return another file as output
'''

import os
import sys

class OneFile():

    def __init__():
        pass

    def load_input_files_from_dir(self, dir):
        if os.path.isdir:
            self.files = os.listdir(dir)
            if len(self.files) == 0:
                # raise ???
                print "Error"

    def get_one_file(self, ordered=True):
        if ordered:
            filenames = sorted(self.files[:])
        else:
            filenames = self.files[:]
        
        for filename in filenames:
            yield filename




