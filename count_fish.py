# Add up the number of creatures in a data file
reader = open('temp.txt', 'r')
for line in reader:
    temp  = line.strip()
    print(line)
reader.close()
