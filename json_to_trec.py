# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 17:47:48 2015

@author: ruhansa
"""
import json
# if you are using python 3, you should
# import urllib.request
import urllib2


with open('test_queries.txt', 'rb') as queries:
    # change the url according to your own koding username and query
    qid = 1
    for line in queries:
        query = line[12:].rstrip()
        inurl= "http://meganarutokage.koding.io:8983/solr/eval/select?q=*" + query + "*&fl=id%2Cscore&wt=json&indent=true&rows=1000"
        outfn = 'BM25results.txt'

        # change query id and IRModel name accordingly
        IRModel= 'BM25'
        outf = open(outfn, 'a+')
        data = urllib2.urlopen(inurl)
        # if you're using python 3, you should use
        # data = urllib.request.urlopen(inurl)

        docs = json.load(data)['response']['docs']
        # the ranking should start from 1 and increase
        rank = 1
        for doc in docs:
            if qid < 10:
                outf.write("00" + str(qid) + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            rank += 1
        qid += 1
    outf.close()
