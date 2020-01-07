"""This script allows use of an IDE (Wing, Pycharm, ...) to debug custom actions:

(-) Place this script in same location as your actions.py
(-) Open & run it from within your IDE
(-) Now you can put breakpoints in your actions.py, but also explore the internals of the
    rasa_sdk action server itself.
"""

import os
import sys

# insert path of this script in syspath so actions.py will be found
sys.path.insert(1, os.path.dirname(os.path.abspath(__file__)))

#
# This is exactly like issuing the command:
#  $ rasa run actions
#
sys.argv.append('run')
sys.argv.append('actions')
sys.argv.append('--actions')
sys.argv.append('demo.actions')
sys.argv.append('--debug')
from rasa.__main__ import main
main()

