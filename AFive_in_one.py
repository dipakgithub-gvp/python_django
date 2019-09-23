
#Data
import mysql.connector
mydata = mysql.connector.connect(host="localhost", user="root", password="root", database="dipak")
mycursor = mydata.cursor()
data = "insert into employee (id, name) values (%s,%s)"
data_value = (1,"Dipak")
mycursor.execute(data, data_value)
mydata.commit()


#2 Methods
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[2:5])
print(len(thistuple))
thistuple[3] = "orange"

thistuple = ("apple",)
print(type(thistuple))
del thistuple
thistuple = tuple(("apple", "banana", "cherry")
thistuple.count(5)
thistuple.index(8)


#11 Methods
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
x = thisdict.get("model")
thisdict["year"] = 2018
thisdict.values()
thisdict.items()
thisdict.keys()
print(len(thisdict))
thisdict.update({"color": "White"})
thisdict.setdefault("model", "Bronco")
thisdict.pop("model")
thisdict.popitem()
del thisdict["model"]
del thisdict
thisdict.clear()
mydict = thisdict.copy()
mydict = dict(thisdict)
thisdict = dict(brand="Ford", model="Mustang", year=1964)
thisdict = dict.fromkeys(x, y)




#11 methods
thislist = ["apple", "banana", "cherry"]

print(len(thislist))
thislist.count("cherry")
thislist.index("cherry")
thislist.reverse()
thislist.append("orange")
thislist.insert(1, "orange")
thislist.remove("banana")
thislist.pop()
thislist.sort()
del thislist[0]
del thislist
thislist.clear()
mylist = thislist.copy()
mylist = list(thislist)
list1.extend(list2)
thislist = list(("apple", "banana", "cherry"))

import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)

#pip install scrapy
#scrapy runspider myspider.py -o out.csv