def laceStrings(s1, s2):
        n = 0
        lace = ''
        if len(s1) > len(s2):
                for n in range(len(s2)):
                        lace += s1[n]
                        lace += s2[n]
                lace += s1[n+1:]
       
        elif len(s2) > len(s1):
                for n in range(len(s1)):
                        lace += s1[n]
                        lace += s2[n]
                lace += s2[n+1:]
       
        else:
                for n in range(len(s1)):
                        lace += s1[n]
                        lace += s2[n]
       
        return lace