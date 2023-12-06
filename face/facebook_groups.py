import csv
import json

from facepy import GraphAPI

"""
Try to get facebook groups comment
"""


def main():
    """
    Try to get comments from facebook API
    :return:
    """
    graph = GraphAPI(
        "EAAB0iARC3rABABfxCB0UZCqM0JubQQWDhAmLcRoJIjDm1uuDCqEFoZCKFSVIMghsDdxoHcyMfeouNZClH5ZCHPkZAyKZB22ZApQPmIQqdu19fu4y9AQPcZBu8lfl6TrPJd0Kh2ULRCcCwBgXpYhcAHr9WWMYbACZB1tURF3ISFvEV5MYlRqon90kwSZCU1NVWYKRcwfPeNco8nvZB7H1BO0b2VZBVve5ASl88LJb43qjkpt9nQZDZD"
    )

    groupIDs = "488606049192077"
    outfile_name = "weores-group-summary.csv"
    f = csv.writer(open(outfile_name, "wb+"))

    data = graph.get(
        groupIDs + "/feed",
        page=False,
        limit=100,
        since="yyyy-mm-dd",
        until="yyyy-mm-dd",
    )
    # data = graph.get(groupIDs + "/feed", retry=3)
    jsonposts = json.dumps(data)
    output = json.loads(jsonposts)
    info = output["data"]
    masterlist = []

    def scrape_data(a):
        for i in a:
            minorlist = [i["created_time"], i["from"]["name"]]
            try:
                minorlist.append(i["name"])
            except:
                minorlist.append("No Link")
            try:
                minorlist.append(i["link"])
            except:
                minorlist.append("No URL")
            try:
                minorlist.append(len(i["likes"]["data"]))
            except KeyError:
                minorlist.append(0)
            try:
                minorlist.append(len(i["comments"]["data"]))
            except KeyError:
                minorlist.append("No Comments :(")
            masterlist.append(minorlist)

    scrape_data(info)

    for item in masterlist:
        try:
            print(", ".join(map(str, item[0:])))
        except UnicodeError:
            pass


if __name__ == "__main__":
    main()
