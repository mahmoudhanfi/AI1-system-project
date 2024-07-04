import os


files = os.listdir('example-solutions/')
for file in files:
    with open('example-solutions/' + file, 'r') as f:
        lines = f.readlines()
        lines[1:] = sorted(lines[1:])

    with open('example-solutions/' + file, 'w') as f:
        f.writelines(lines)