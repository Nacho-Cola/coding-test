def chage_sh(data) :
    data = data.replace('C#', 'c')
    data = data.replace('D#', 'd')
    data = data.replace('F#', 'f')
    data = data.replace('G#', 'g')
    data = data.replace('A#', 'a')

    return data

def solution(m, musicinfos):
    m = chage_sh(m)
    table = []
    answer = {}
    for ls in musicinfos:
        table.append(ls.split(","))
    for i in table:
        h1, m1  = i[0].split(":")
        h2, m2  = i[1].split(":")
        dt = (int(h2) - int(h1)) * 60 + (int(m2) - int(m1))
        i[0] = dt
        i[-1] = chage_sh(i[-1])
        i[-1] = i[-1] * (dt//len(i[-1])) + i[-1][0:dt%len(i[-1])]        
        
    for ind in table:
        if m in ind[-1]:
            answer[ind[-2]] = ind[0]
    

    return sorted(answer.items(), key=lambda x: x[1], reverse = True)[0][0] if answer else '(None)'