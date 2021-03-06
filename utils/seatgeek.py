import urllib2, json, requests,dateutil.parser, sorts, keyReader
from requests import auth
from requests.auth import HTTPBasicAuth

#
#    Input: Single word query
#  Returns: List of events relevant to the query in New York and information separated in a list of entries
#
#           Format for entries in fullList: [organization, event, performance, url, time, ticket type, price, seat]
#
def seatgeek(query):

    fullList = []

    seatGeek_key = keyReader.returnKey("seatGeek")

    link = "https://api.seatgeek.com/2/events?q="+query.replace(" ","+")+"&venue.state=NY&client_id=" + seatGeek_key
    u = urllib2.urlopen(link)
    response = u.read()
    data = json.loads(response)

    events = data['events']

    # Events
    for i in events:
        
        orgName = "N/A"
        eventName = i['title']
        url = i['url']
        time = i['datetime_utc']
        ticket_type = "N/A"
            
        seat = "N/A"

        # Performances
        for j in i['performers']:

            
            price = "N/A"
        
            try:
                float(i['stats']['average_price'])
                price = i['stats']['average_price'] # seatgeek does not show ticket types nor specific prices or seats
            except:
                price = 999999 # will allow undefined price to sink when sorted

            
            entry = []
            perfName = j['name']

            entry.append(orgName)
            entry.append(eventName)
            entry.append(perfName)
            entry.append(url)

            # conversion from datetime obj to string allows for easier comparison
            entry.append(str(dateutil.parser.parse(time))) # datetime: year, month, day, hour, minute, second
            
            entry.append(ticket_type)
            entry.append(price)
            entry.append(seat)
            entry.append("Seat Geek")
            fullList.append(entry)

    return fullList


## TESTING ##

#def main():
##     #listF = byAlphaEventDes("music")
##     #for i in listF:
##         #print(i[1])

#    fullList = seatgeek("music")
#    orderList = sorts.byPriceAsc(fullList)
#    for i in orderList:
#        print(i[1] + " | Price:" + str(i[6]) )
        
#main()
