#!/usr/bin/env python
#Importing Packages and Modules (ways of importing them)

import sys
sys.path.append('/home/mkseth/VENV/py311_venv/lib/python3.12/site-packages/testpackage')
print(sys.path)

'''
import mymainpackage.mainscript
import mymainpackage.subpackage.subscript

mymainpackage.mainscript.main_report()
mymainpackage.subpackage.subscript.sub_report()
'''

from mymainpackage import mainscript as mod1, mymodule as mod3
from mymainpackage.subpackage import subscript as mod2

'''
mainscript.main_report()
subscript.sub_report()
mymodule.my_func()
'''

mod1.main_report()
mod2.sub_report()
mod3.my_func()

'''
from mymainpackage.mainscript import main_report as mreport
from mymainpackage.mymodule import my_func as mainfunc
from mymainpackage.subpackage.subscript import sub_report as sreport

main_report()
my_func()
sub_report()

mreport()
mainfunc()
sreport()
'''

##
##End of file
