import sys

#name_1= sys.argv[1]
#name_2= sys.argv[2]
#name_3= sys.argv[3]

theList= [sys.argv[1].lower(),sys.argv[2].lower(),sys.argv[3].lower()]

# each line one response(name)
for br in sorted(theList):
  print(br)
