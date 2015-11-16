import json

outf = open('BM25results.txt', 'a+')

with open('russBM25.json') as data:
    docs = json.load(data)
# the ranking should start from 1 and increase

IRModel = 'default'
qid= '010'

rank = 1
for doc in docs:
    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
    rank += 1
outf.close()
