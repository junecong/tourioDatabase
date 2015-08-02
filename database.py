# -*- coding: utf-8 -*-

import sqlite3
db = sqlite3.connect('tourio.db')

#Comments Table
db.execute("CREATE TABLE tours (id INTEGER PRIMARY KEY, TourName TEXT, TourDescription TEXT, Rating INTEGER, Duration INTEGER, UserID INTEGER, CityID INTEGER);")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Perfect SF Hipster Sunday', 'Spend some time in the more alternative parts of SF, like the Castro and Haight-Ashbury. Experience the hippie culture for yourself, and dont forget your Tartine pastry!', 5, 3, 1, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Extreme SF', 'Who says you cant do outdoorsy things in a big city?', 5, 3, 1, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Scenic Views and Picnic Foods', 'Check out the beautiful views of SF, like Sutro Baths, Lands End, and Crissy Field. In between, enjoy a picnic at Baker Beach', 4, 4, 1, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Chi-town Low Dow', 'Get the low down on the best town around', 5, 3, 1, 3)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Chicago Art Walk', 'With the Art Institute, MCA, The Picasso, and everything else, Chicago has one of the best art scenes around. Learn more in this tour through the city.', 5, 2, 1, 3)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Midwest Feel in a Big City Town', 'Just because Chicago is a big city doesnt mean were not still in the Midwest. These are some of the nicest places to go in the city.', 4, 4, 1, 3)")

# Users Table
db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, email TEXT, pass TEXT, imageUrl TEXT, city TEXT);")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('June', 'Cong', 'junzhucong@gmail.com', 'password', 'https://scontent.xx.fbcdn.net/hphotos-xtp1/v/t1.0-9/10897901_10153199942450240_3191792129415226488_n.jpg?oh=fd7022e82fa0ac2591548125a09d8750&oe=5658B341', 'Berkeley')")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('Shawn', 'Huang', 'admin@gmail.com', 'password', 'https://scontent.xx.fbcdn.net/hphotos-xtp1/v/t1.0-9/10897901_10153199942450240_3191792129415226488_n.jpg?oh=fd7022e82fa0ac2591548125a09d8750&oe=5658B341', 'Berkeley')")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('Prudhvil', 'Lokireddy', 'admin@gmail.com', 'password', 'https://scontent.xx.fbcdn.net/hphotos-xtp1/v/t1.0-9/10897901_10153199942450240_3191792129415226488_n.jpg?oh=fd7022e82fa0ac2591548125a09d8750&oe=5658B341', 'Berkeley')")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('Aim', 'Phongpandecha', 'admin@gmail.com', 'password', 'https://scontent.xx.fbcdn.net/hphotos-xtp1/v/t1.0-9/10897901_10153199942450240_3191792129415226488_n.jpg?oh=fd7022e82fa0ac2591548125a09d8750&oe=5658B341', 'Berkeley')")


# Stops Table
db.execute("CREATE TABLE stops (id INTEGER PRIMARY KEY, TourID INTEGER, Name TEXT, TourIndex INTEGER, Description TEXT, Lat INTEGER, Long INTEGER, Pic1 TEXT);")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (1, 'Mission Street Art', 1, 'Clarion Alley is a small street in San Francisco between Mission and Valencia Streets and 17th and 18th Streets, notable for the murals painted by the Clarion Alley Mural Project.', 37.763062, -122.419523, 'https://commons.wikimedia.org/wiki/File:CAMP_2012.jpg#/media/File:CAMP_2012.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (1, 'Brunch at Kitch Story', 2, 'At Kitchen Story, a new restaurant in San Franciscos Castro neighborhood, lunchtime diners come for the bacon—and return for Asian-influenced California cuisine.', 37.764176, -122.430668, 'http://junecong.com')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (1, 'Haight Ashbury Shopping', 3, 'Haight-Ashbury is known for its history of being the origin of hippie subculture. The thrift stores that line the streets are some of the most unique in the city.', 37.769958, -122.446961, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (1, 'Afternoon Coffee at Tartine', 4, 'Organic ingredients provide the makings for breakfast pastries, hot pressed sandwiches & coffee.', 37.761418, -122.424104, 'http://s3-media4.fl.yelpcdn.com/bphoto/SG0NJG1prp5RC11UfshF7Q/o.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (1, 'Relax at Dolores Park', 5, 'Encompassing nearly 16 acres, Mission Dolores Park is one of SFs most popular parks, the vibrant heart of its culturally diverse neighborhood. Many festivals, performances, and other cultural events are held here, and on sunny afternoons people flock to the park to play, picnic, lounge, and enjoy spectacular views of the city\’s skyline and beyond.', 37.759773, -122.427063, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg')")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (2, 'Mission Street Art', 1, 'Clarion Alley is a small street in San Francisco between Mission and Valencia Streets and 17th and 18th Streets, notable for the murals painted by the Clarion Alley Mural Project.', 37.763062, -122.419523, 'https://commons.wikimedia.org/wiki/File:CAMP_2012.jpg#/media/File:CAMP_2012.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (2, 'Brunch at Kitch Story', 2, 'At Kitchen Story, a new restaurant in San Franciscos Castro neighborhood, lunchtime diners come for the bacon—and return for Asian-influenced California cuisine.', 37.764176, -122.430668, 'http://si.wsj.net/public/resources/images/SF-AB925_LUNCHB_P_20130109105149.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (2, 'Haight Ashbury Shopping', 3, 'Haight-Ashbury is known for its history of being the origin of hippie subculture. The thrift stores that line the streets are some of the most unique in the city.', 37.769958, -122.446961, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (2, 'Afternoon Coffee at Tartine', 4, 'Organic ingredients provide the makings for breakfast pastries, hot pressed sandwiches & coffee.', 37.761418, -122.424104, 'http://s3-media4.fl.yelpcdn.com/bphoto/SG0NJG1prp5RC11UfshF7Q/o.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (2, 'Relax at Dolores Park', 5, 'Encompassing nearly 16 acres, Mission Dolores Park is one of SFs most popular parks, the vibrant heart of its culturally diverse neighborhood. Many festivals, performances, and other cultural events are held here, and on sunny afternoons people flock to the park to play, picnic, lounge, and enjoy spectacular views of the city\’s skyline and beyond.', 37.759773, -122.427063, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg')")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (3, 'Mission Street Art', 1, 'Clarion Alley is a small street in San Francisco between Mission and Valencia Streets and 17th and 18th Streets, notable for the murals painted by the Clarion Alley Mural Project.', 37.763062, -122.419523, 'https://commons.wikimedia.org/wiki/File:CAMP_2012.jpg#/media/File:CAMP_2012.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (3, 'Brunch at Kitch Story', 2, 'At Kitchen Story, a new restaurant in San Franciscos Castro neighborhood, lunchtime diners come for the bacon—and return for Asian-influenced California cuisine.', 37.764176, -122.430668, 'http://si.wsj.net/public/resources/images/SF-AB925_LUNCHB_P_20130109105149.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (3, 'Haight Ashbury Shopping', 3, 'Haight-Ashbury is known for its history of being the origin of hippie subculture. The thrift stores that line the streets are some of the most unique in the city.', 37.769958, -122.446961, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (3, 'Afternoon Coffee at Tartine', 4, 'Organic ingredients provide the makings for breakfast pastries, hot pressed sandwiches & coffee.', 37.761418, -122.424104, 'http://s3-media4.fl.yelpcdn.com/bphoto/SG0NJG1prp5RC11UfshF7Q/o.jpg')")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1) VALUES (3, 'Relax at Dolores Park', 5, 'Encompassing nearly 16 acres, Mission Dolores Park is one of SFs most popular parks, the vibrant heart of its culturally diverse neighborhood. Many festivals, performances, and other cultural events are held here, and on sunny afternoons people flock to the park to play, picnic, lounge, and enjoy spectacular views of the city\’s skyline and beyond.', 37.759773, -122.427063, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg')")

# Comments Table
db.execute("CREATE TABLE comments (id INTEGER PRIMARY KEY, TourID INTEGER, Comment TEXT, Rating INTEGER, Time INTEGER, CommenterID INTEGER);")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'I really loved the street art aspect of this tour, thanks for showing us around!', 5, 201508050109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'I now dream of Tartine morning buns. Thanks so much!', 5, 201508010109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'Found my new favorite Cafe!', 5, 201508040109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'Tour felt a little long to me, we just stopped after Haight-Ashbury because the shops werent really our style', 3, 201508030109, 1)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'I really loved the street art aspect of this tour, thanks for showing us around!', 5, 201508050109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'I now dream of Tartine morning buns. Thanks so much!', 5, 201508010109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'Found my new favorite Cafe!', 5, 201508040109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'Tour felt a little long to me, we just stopped after Haight-Ashbury because the shops werent really our style', 3, 201508030109, 1)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'I really loved the street art aspect of this tour, thanks for showing us around!', 5, 201508050109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'I now dream of Tartine morning buns. Thanks so much!', 5, 201508010109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'Found my new favorite Cafe!', 5, 201508040109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'Tour felt a little long to me, we just stopped after Haight-Ashbury because the shops werent really our style', 3, 201508030109, 1)")




db.commit()
