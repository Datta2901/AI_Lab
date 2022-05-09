def ToGoOut():
    answer = list()
    for g in range(0,10):
        for o in range(0,10):
            for t in range(0,10):
                for u in range(0,10):
                    #    g o
                    #(+) t o
                    #----------
                    #  o u t
                    #-----------
                    if len(set([g, o, t, u])) == 4:
                        go = 10 * g + o
                        to = 10 * t + o
                        out = 100 * o + 10 * u + t

                        if go + to == out:
                            answer.append((go, to, out))
    return answer

print(ToGoOut())
