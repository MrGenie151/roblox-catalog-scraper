import requests

category = input("Enter A Category: ")
#print(catagory)
subcategory = input("Enter A Subcategory: ")
#print(subcatagory)
nextpcursor  = input("Enter Next Page Cursor (optional): ")

url = "https://catalog.roblox.com/v1/search/items/details?Category="+category+"&Limit=30&SortAggregation=5&SortType=2&Subcategory="+subcategory
if nextpcursor:
    url = url + "&Cursor=" + nextpcursor

r = requests.get(url)
#print(url)

directory = "./cscraper-results/"
filepath = directory + input("Enter a filname: ") + ".json"
Ids = []
rj = r.json()
with open(filepath,"w+") as fp:
    for data in rj['data']:
        Ids.append(data['id'])
    fp.write(str(Ids))
print("Next Page Cursor: " + rj['nextPageCursor'])
