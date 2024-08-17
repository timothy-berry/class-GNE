#!/usr/bin/env python

import sys
sys.path.append('/home/mkseth/VENV/py311_venv/lib/python3.12/site-packages/testpackage')
print(sys.path)

from mymainpackage import mainscript
from mymainpackage import mymodule
from mymainpackage.subpackage import subscript

mainscript.main_report()

subscript.sub_report()

mymodule.my_func()
