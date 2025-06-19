import sys
args = sys.argv[1:]
if len(args) != 1:
    print("none")
else:
    string = args[0]
    count_z = string.count('z')
    if count_z > 0:
        print("z" * count_z)
    else:
        print("none")