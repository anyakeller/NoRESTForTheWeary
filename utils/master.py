# Compilation of Master Sorted Lists Module
#
# Orders master list of each list returned by an api when requesting events related to <query>
#

#import utils.sorts,utils.ticketleap,utils.ticketmaster,utils.seatgeek
import sorts,ticketleap,ticketmaster,seatgeek

# orders entries by price in ascending order
# takes in query string and upper and lower bounds on price
def byPriceAsc(query,minP,maxP):

    # leapList = utils.ticketleap.ticketleap(query)
    # masterList = utils.ticketmaster.ticketmaster(query)
    # geekList = utils.seatgeek.seatgeek(query)

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    # fullList = utils.sorts.byPriceAsc(fullList)

    fullList = sorts.byPriceAsc(fullList)

    # return utils.sorts.priceRange(fullList,minP,maxP)

    return sorts.priceRange(fullList,minP,maxP)

# orders entries by price in descending order
# takes in query string and upper and lower bounds on price
def byPriceDes(query,minP,maxP):

    # leapList = utils.ticketleap.ticketleap(query)
    # masterList = utils.ticketmaster.ticketmaster(query)
    # geekList = utils.seatgeek.seatgeek(query)

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    # fullList = utils.sorts.byPriceDes(fullList)

    fullList = sorts.byPriceDes(fullList)
    
    # return utils.sorts.priceRange(fullList,minP,maxP)

    return sorts.priceRange(fullList,minP,maxP)

# orders entries by date in ascending order
# takes in query string and upper and lower bounds on price
def byDateAsc(query,minP,maxP):

    # leapList = utils.ticketleap.ticketleap(query)
    # masterList = utils.ticketmaster.ticketmaster(query)
    # geekList = utils.seatgeek.seatgeek(query)

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    # fullList = utils.sorts.byDateAsc(fullList)

    fullList = sorts.byDateAsc(fullList)

    # return utils.sorts.priceRange(fullList,minP,maxP)

    return sorts.priceRange(fullList,minP,maxP)

# orders entries by date in descending order
# takes in query string and upper and lower bounds on price
def byDateDes(query,minP,maxP):

    # leapList = utils.ticketleap.ticketleap(query)
    # masterList = utils.ticketmaster.ticketmaster(query)
    # geekList = utils.seatgeek.seatgeek(query)

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    # fullList = utils.sorts.byDateDes(fullList)

    fullList = sorts.byDateDes(fullList)

    # return utils.sorts.priceRange(fullList,minP,maxP)

    return sorts.priceRange(fullList,minP,maxP)

# orders entries alphabetically in ascending order
# takes in query string and upper and lower bounds on price
def byAlphaEventAsc(query,minP,maxP):

    # leapList = utils.ticketleap.ticketleap(query)
    # masterList = utils.ticketmaster.ticketmaster(query)
    # geekList = utils.seatgeek.seatgeek(query)

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    # fullList = utils.sorts.byAlphaEventAsc(fullList)

    fullList = sorts.byAlphaEventAsc(fullList)

    # return utils.sorts.priceRange(fullList,minP,maxP)

    return sorts.priceRange(fullList,minP,maxP)

# orders entries alphabetically in descending order
# takes in query string and upper and lower bounds on price
def byAlphaEventDes(query,minP,maxP):

    # leapList = utils.ticketleap.ticketleap(query)
    # masterList = utils.ticketmaster.ticketmaster(query)
    # geekList = utils.seatgeek.seatgeek(query)

    leapList = ticketleap.ticketleap(query)
    masterList = ticketmaster.ticketmaster(query)
    geekList = seatgeek.seatgeek(query)

    fullList = leapList + masterList + geekList

    # fullList = utils.sorts.byAlphaEventDes(fullList)

    fullList = sorts.byAlphaEventDes(fullList)

    # return utils.sorts.priceRange(fullList,minP,maxP)

    return sorts.priceRange(fullList,minP,maxP)

## Testing ##


# def main():
#     listF = byDateAsc("music",0,900)

#     for i in listF:
#         print(i[4])

# main()

