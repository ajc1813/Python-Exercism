#def rectangles(strings):
    #pass

def rectangles(strings):
    cnt = 0
    for r in range(len(strings)):
        for i in range(len(strings[r])):
            if strings[r][i]=="+":
                for j in range(i+1, len(strings[r])):
                    if strings[r][j] in " |": break
                    elif strings[r][j]=="+":
                        for k in range(r+1, len(strings)):
                            if strings[k][i] == "+" and strings[k][j] == "+":
                                if not " " in strings[k][i+1:j] and not "|" in strings[k][i+1:j]: cnt += 1
                            elif strings[k][i] not in "+|" or strings[k][j] not in "+|": break
    return cnt