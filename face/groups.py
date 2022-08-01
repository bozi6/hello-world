import csv
import json

from facepy import GraphAPI

graph = GraphAPI(
    'EAAB0iARC3rABABfxCB0UZCqM0JubQQWDhAmLcRoJIjDm1uuDCqEFoZCKFSVIMghsDdxoHcyMfeouNZClH5ZCHPkZAyKZB22ZApQPmIQqdu19fu4y9AQPcZBu8lfl6TrPJd0Kh2ULRCcCwBgXpYhcAHr9WWMYbACZB1tURF3ISFvEV5MYlRqon90kwSZCU1NVWYKRcwfPeNco8nvZB7H1BO0b2VZBVve5ASl88LJb43qjkpt9nQZDZD')

groupIDs = ("488606049192077")
outfile_name = "weores-group-summary.csv"
f = csv.writer(open(outfile_name, "wb+"))

data = graph.get(groupIDs + '/feed', page=False, limit=100, since="yyyy-mm-dd", until="yyyy-mm-dd")
# data = graph.get(groupIDs + "/feed", retry=3)
jsonposts = json.dumps(data)
output = json.loads(jsonposts)
info = output[u'data']
masterlist = []


def scrape_data(a):
    for i in a:
        minorlist = [i[u'created_time'], i[u'from'][u'name']]
        try:
            minorlist.append(i[u'name'])
        except:
            minorlist.append("No Link")
        try:
            minorlist.append(i[u'link'])
        except:
            minorlist.append("No URL")
        try:
            minorlist.append(len(i[u'likes'][u'data']))
        except KeyError:
            minorlist.append(0)
        try:
            minorlist.append(len(i[u'comments'][u'data']))
        except KeyError:
            minorlist.append("No Comments :(")
        masterlist.append(minorlist)


scrape_data(info)

for item in masterlist:
    try:
        print(", ".join(map(str, item[0:])))
    except UnicodeError:
        pass
