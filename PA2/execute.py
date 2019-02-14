#!/usr/bin/env python
import os
import subprocess
subprocess.call("rm -f ./a.out", shell=True)
retcode = subprocess.call("./test.sh", shell=True)
print("Two tests have been run!")
print ("You got " + str(retcode) + " out of 2 correct.")
if int(retcode) == 2:
    print("Congratulations!")
else:
    print("Please Fix Your Code!")
print("\n")
print("*************Your Code Below*************")
with open('add.py','r') as fs:
 print(fs.read())
