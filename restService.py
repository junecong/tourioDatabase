import json
import bottle
import sqlite3
from bottle import route, run, request, abort, template, response
from json import dumps


db = sqlite3.connect('tourio.db')
c = db.cursor()

@route('/')
def basic_function():
    print "Hi Prud"

#get all comments for this tour
@route('/comments/<tourIdGiven>', method='GET')
def get_comments_for_tour(tourIdGiven):
    
    c.execute('SELECT TourID,Comment,Rating,Time,CommenterID FROM comments WHERE TourID = ?', (tourIdGiven))
    data = [dict((c.description[i][0], value) \
        for i, value in enumerate(row)) for row in c.fetchall()]

    listToAppend = []
    
    for i in data:
        holderID = data[0]["CommenterID"]
        c.execute('SELECT FirstName,imageUrl FROM users WHERE id = (?)', (holderID,))
        user = [dict((c.description[j][0], value) \
        for j, value in enumerate(row)) for row in c.fetchall()]

        user.append(i)
        listToAppend.append(user)        

    if not listToAppend:
        abort(404, 'No document with id %s' % id)

    response.content_type = 'application/json'
    return json.dumps(listToAppend)


#get all tours for this city
@route('/city/<cityIdGiven>', method='GET')
def get_tours_by_city(cityIdGiven):
    
    c.execute('SELECT id,TourName,Rating,Duration FROM tours WHERE CityID = (?)', (cityIdGiven,))

    tours = [dict((c.description[i][0], value) \
        for i, value in enumerate(row)) for row in c.fetchall()]

    listToAppend = []

    for i in tours:
        holderID = i["id"]
        c.execute('SELECT lat,long,TourIndex,Pic1 FROM stops WHERE TourID = (?) ORDER BY TourIndex ASC', (holderID,))
        stops = [dict((c.description[j][0], value) \
        for j, value in enumerate(row)) for row in c.fetchall()]

        listToAppend.append(i)
        listToAppend.append(stops)

    # if not tours:
    #     abort(404, 'No document with id %s' % id)
    # c.close()

    response.content_type = 'application/json'
    return json.dumps(listToAppend)

#get all detais for this tour
@route('/tour/<tourIdGiven>', method='GET')
def get_tour(tourIdGiven):
    
    c.execute('SELECT TourName,TourDescription,Rating,Duration,UserID,CityID FROM tours WHERE id = (?)', (tourIdGiven,))

    tour = [dict((c.description[i][0], value) \
        for i, value in enumerate(row)) for row in c.fetchall()]

    holderID = tour[0]["UserID"]
    c.execute('SELECT FirstName,imageUrl FROM users WHERE id = (?)', (holderID,))
    userDetails = [dict((c.description[j][0], value) \
        for j, value in enumerate(row)) for row in c.fetchall()]

    tour.append(userDetails)

    c.execute('SELECT Name,TourIndex,Description,Lat,Long,Pic1,Category FROM stops WHERE TourID = (?) ORDER BY TourIndex ASC', (tourIdGiven,))
    stops = [dict((c.description[j][0], value) \
        for j, value in enumerate(row)) for row in c.fetchall()]

    tour.append(stops)


    c.execute('SELECT CommenterID,Comment,Rating,Time FROM comments WHERE TourID = (?) ORDER BY Time ASC', (tourIdGiven,))
    comments = [dict((c.description[j][0], value) \
        for j, value in enumerate(row)) for row in c.fetchall()]


    for i in comments:
        holder = i["CommenterID"]
        c.execute('SELECT FirstName,LastName,imageUrl FROM users WHERE id = (?)', (holder,))
        commenter = [dict((c.description[j][0], value) \
        for j, value in enumerate(row)) for row in c.fetchall()]

        tour.append(commenter)
        tour.append(i)

    # if not tour:
    #     abort(404, 'No document with id %s' % id)
    # c.close()

    response.content_type = 'application/json'
    return json.dumps(tour)

@route('/user/<userIdGiven>', method='GET')
def get_user(userIdGiven):
    
    c.execute('SELECT FirstName,LastName,imageUrl,city FROM users WHERE id = (?)', (userIdGiven))
    user = [dict((c.description[i][0], value) \
        for i, value in enumerate(row)) for row in c.fetchall()]

    # if not user:
    #     abort(404, 'No document with id %s' % id)

    response.content_type = 'application/json'
    return json.dumps(user)



@route('/rating/<no:int>/<rate:int>', method='POST')
def edit_item(no, rate):

    intno = int(no)

    c.execute('SELECT Rating,RatingNum FROM tours WHERE id = (?)', (intno,))


    ratinglist = [dict((c.description[i][0], value) \
        for i, value in enumerate(row)) for row in c.fetchall()]

    oldrating =  ratinglist[0].get('Rating')
    oldratingnum = ratinglist[0].get('RatingNum')


    newratingnum = int(oldratingnum) + 1

    newrating = rate

    intnew = (((oldrating * oldratingnum) + newrating) / newratingnum)

    c.execute("UPDATE tours SET RatingNum = ? WHERE id LIKE ?", (newratingnum, no))
    c.execute("UPDATE tours SET Rating = ? WHERE id LIKE ?", (newrating, no))


    return 'Success'



#run this shit
run(host='0.0.0.0', port=5000)
