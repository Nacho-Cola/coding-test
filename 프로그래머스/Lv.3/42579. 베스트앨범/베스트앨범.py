def solution(genres, plays):
    answer = []
    rank = {}
    time = {}
    for i, gen, play in zip(range(len(plays)), genres, plays):
        if gen in rank:
            rank[gen][i]=play
        else:
            rank[gen] = {i:play}
    for gen, play in rank.items():
        rank[gen][-1] = sum(play.values())
    rank = sorted(rank.values(), key = lambda x: x[-1], reverse = True)
    for i in rank:
        i = sorted(i.items(), key=lambda x: x[1], reverse=True)
        if len(list(dict(i).keys())) > 2 :
            answer += (list(dict(i).keys())[1:3])
        else:
            answer += (list(dict(i).keys())[0:1])   
    return answer