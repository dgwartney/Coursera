import sys
import unittest

class Writer(object):
    log = ""

    def write(self, data):
        self.log = self.log + data

    def getLog(self):
        return self.log


w = Writer()

w.write("Hello")
print(w.getLog())


import sys
from io import TextIOWrapper, BytesIO

# setup the environment
old_stdout = sys.stdout
sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)

# do something that writes to stdout or stdout.buffer
print('Hello World!')

# get output
sys.stdout.seek(0)      # jump to the start
out = sys.stdout.read() # read output

# restore stdout
sys.stdout.close()
sys.stdout = old_stdout

print(out)



