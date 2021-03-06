import urllib2, json, requests, dateutil.parser, sorts, keyReader
from requests import auth
from requests.auth import HTTPBasicAuth

#
#    Input: Single word query
#  Returns: List of events relevant to the query in New York and information separated in a list of entries
#
#           Format for entries in fullList: [organization, event, performance, url, time, ticket type, price, seat]
#
def ticketmaster(query):

    q = query.split(" ")[0]

    fullList = []

    ticketMaster_key = keyReader.returnKey("ticketMaster")

    link = "https://app.ticketmaster.com/discovery/v2/events.json?keyword="+q+"&dmaId=345&apikey="+ticketMaster_key
    u = urllib2.urlopen(link)
    response = u.read()
    data = json.loads(response)
    events = []

    # in the case that q is irrelevant to any events and data is returned as an empty dictionary
    if('_embedded' in data):
        events = data['_embedded']['events']

    # Events
    for i in events:

        orgName = "Ticketmaster"
        eventName = i['name']
        perfName = i['name']
        url = i['url']
        time = i['dates']['start']['localDate']
        if(i['dates']['start']['timeTBA']):
            time += " Time TBA"
        elif(i['dates']['start']['noSpecificTime']):
            time += " Time N/A"
        else:
            time = i['dates']['start']['dateTime']

        ticket_type = "N/A"
        price = "N/A"
        seat = "N/A"
        entry = []

        # Priceranges for each ticket (1 or more ticket types)
        if('priceRanges' in i):
            for p in i['priceRanges']:
                ticket_type = p['type']
                price = round(float(p['min']),2)

                entry.append(orgName)
                entry.append(eventName)
                entry.append(perfName)
                entry.append(url)
                
                # conversion of date from datetime obj to string allows for easy comparison
                if not "TBA" in time and not "N/A" in time:
                    entry.append(str(dateutil.parser.parse(time))) 
                else:
                    entry.append(time)
                    
                entry.append(ticket_type)
                entry.append(price)
                entry.append(seat)
                entry.append("Ticket Master")
                fullList.append(entry)
                
        else: # no defined ticket type/price range
            
            entry.append(orgName)
            entry.append(eventName)
            entry.append(perfName)
            entry.append(url)
            entry.append(time)
            entry.append(ticket_type)
            entry.append("N/A: Price not Defined")
            entry.append(seat)
            entry.append("Ticket Master")

            fullList.append(entry)


    return fullList

## TESTING ##

#def main():
#   fullList = ticketmaster("new york")
#    orderedList = sorts.byDateAsc(fullList)
#    priceRange = sorts.priceRange(orderedList,10,140)
#    for i in priceRange:
#        print(i[1] + " | Price:" + str(i[6]) + " | Time:" + str(i[4]) )


#main()
    
