import os
import json
def getdata(path_data = 'data/sogou'):
    D = {}
    f_r = open(os.path.join(path_data,'train.txt'),'r')
    f_w = open(os.path.join(path_data,'train_test.txt'),'w')
    for line in f_r:
        s = list(line.strip())
        for i in range(len(s)):
            if s[i] not in D:
                D[s[i]] = len(D)
        f_w.write(' '.join(list(line)))
    f_w.close()
    f_r.close()
    f_r = open(os.path.join(path_data, 'valid.txt'), 'r')
    f_w = open(os.path.join(path_data, 'valid_test.txt'), 'w')
    for line in f_r:
        s = list(line.strip())
        for i in range(len(s)):
            if s[i] not in D:
                D[s[i]] = len(D)
        f_w.write(' '.join(list(line)))
    f_w.close()
    f_r.close()
    D['<unk>'] = len(D)
    with open('output_test/vocab.json','w') as f:
        json.dump(D,f,ensure_ascii=False)