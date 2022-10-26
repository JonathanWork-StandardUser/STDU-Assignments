import argparse

parser = argparse.ArgumentParser()
parser.add_argument("length", type = int, help="Enter length of password to be.")
args = parser.parse_args()

print(args)
#for x in args