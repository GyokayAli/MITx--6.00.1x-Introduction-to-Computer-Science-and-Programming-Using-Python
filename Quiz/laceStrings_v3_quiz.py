def laceStrings(s1, s2):
    shorter, longer = sorted([s1, s2], key=len)
    output = []
    for i in range(len(shorter)):
        output.append(s1[i])
        output.append(s2[i])
    output += longer[len(shorter):]
    return "".join(output)