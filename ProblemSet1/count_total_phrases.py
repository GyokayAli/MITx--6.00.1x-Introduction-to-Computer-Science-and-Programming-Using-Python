string = "bobovdolnabobobo"
search = "bob"
print "Number of times bob occur is:",
print len([i for i in range(len(string)) if string.startswith(search, i)])