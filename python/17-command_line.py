# Write a Python program to get the command-line arguments
import sys

args = len(sys.argv) - 1
print ("The script was called with %i arguments" % (args))
print("Arguments : " + " ".join(sys.argv[1::]))