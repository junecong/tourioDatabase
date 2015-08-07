# -*- coding: utf-8 -*-

import sqlite3
db = sqlite3.connect('tourio.db')

#Comments Table
db.execute("CREATE TABLE tours (id INTEGER PRIMARY KEY, TourName TEXT, TourDescription TEXT, Rating INTEGER, Duration INTEGER, UserID INTEGER, CityID INTEGER);")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Perfect SF Hipster Sunday', 'Spend some time in the more alternative parts of SF, like the Castro and Haight-Ashbury. Experience the hippie culture for yourself, and dont forget your Tartine pastry!', 5, 3, 1, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Extreme SF', 'Who says you cant do outdoorsy things in a big city?', 4, 3, 1, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Scenic Views and Picnic Foods', 'Check out the beautiful views of SF, like Sutro Baths, Lands End, and Crissy Field. In between, enjoy a picnic at Baker Beach', 3, 4, 1, 1)")

#testing tours below
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('SF Pub Crawl', 'You know what this is.', 3, 2, 4, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Get To Know Berkeley', 'Berkeley is the number on Public University in the world! Learn more about it while living the life of an undergraduate student.', 5, 1, 3, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Downtown Lowdown', 'See what SF Downtown is all about', 5, 2, 4, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Heritage of the City', 'Visit the different ethnic areas of SF and experience new cultures', 5, 5, 2, 1)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Startup Walk', 'See the tech areas and where all the local techies hang out.', 5, 1, 3, 1)")



db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Chi-town Low Dow', 'Get the low down on the best town around', 5, 3, 1, 3)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Chicago Art Walk', 'With the Art Institute, MCA, The Picasso, and everything else, Chicago has one of the best art scenes around. Learn more in this tour through the city.', 5, 2, 1, 3)")
db.execute("INSERT INTO tours (TourName,TourDescription,Rating,Duration,UserID,CityID) VALUES ('Midwest Feel in a Big City Town', 'Just because Chicago is a big city doesnt mean were not still in the Midwest. These are some of the nicest places to go in the city.', 3, 4, 1, 3)")

# Users Table
db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, FirstName TEXT, LastName TEXT, email TEXT, pass TEXT, imageUrl TEXT, city TEXT);")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('June', 'Cong', 'junzhucong@gmail.com', 'password', 'http://junecong.com/img/tourioImages/june.jpg', 'Berkeley')")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('Shawn', 'Huang', 'admin@gmail.com', 'password', 'http://junecong.com/img/tourioImages/shawn.jpg', 'Berkeley')")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('Prudhvil', 'Lokireddy', 'admin@gmail.com', 'password', 'http://junecong.com/img/tourioImages/prud.jpg', 'Berkeley')")
db.execute("INSERT INTO users (FirstName,LastName,email,pass,imageUrl,city) VALUES ('Aim', 'Phongpandecha', 'admin@gmail.com', 'password', 'http://junecong.com/img/tourioImages/aim.jpg', 'Berkeley')")


# Stops Table
db.execute("CREATE TABLE stops (id INTEGER PRIMARY KEY, TourID INTEGER, Name TEXT, TourIndex INTEGER, Description TEXT, Lat INTEGER, Long INTEGER, Pic1 TEXT, Category INTEGER);")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (1, 'Mission Street Art', 1, 'Clarion Alley is a small street in San Francisco between Mission and Valencia Streets and 17th and 18th Streets, notable for the murals painted by the Clarion Alley Mural Project.', 37.763062, -122.419523, 'https://upload.wikimedia.org/wikipedia/commons/8/85/CAMP_2012.jpg', 1)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (1, 'Brunch at Kitchen Story', 2, 'At Kitchen Story, a new restaurant in San Franciscos Castro neighborhood, lunchtime diners come for the bacon—and return for Asian-influenced California cuisine.', 37.764176, -122.430668, 'http://s3-media1.fl.yelpcdn.com/bphoto/ttVmYYSvxAJwINqhDZJZZA/ls.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (1, 'Haight Ashbury Shopping', 3, 'Haight-Ashbury is known for its history of being the origin of hippie subculture. The thrift stores that line the streets are some of the most unique in the city.', 37.769958, -122.446961, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (1, 'Afternoon Coffee at Tartine', 4, 'Organic ingredients provide the makings for breakfast pastries, hot pressed sandwiches & coffee.', 37.761418, -122.424104, 'http://s3-media4.fl.yelpcdn.com/bphoto/SG0NJG1prp5RC11UfshF7Q/o.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (1, 'Relax at Dolores Park', 5, 'Encompassing nearly 16 acres, Mission Dolores Park is one of SFs most popular parks, the vibrant heart of its culturally diverse neighborhood.', 37.759773, -122.427063, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg', 4)")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (2, 'Mission Street Art', 1, 'Clarion Alley is a small street in San Francisco between Mission and Valencia Streets and 17th and 18th Streets, notable for the murals painted by the Clarion Alley Mural Project.', 37.763062, -122.419523, 'https://upload.wikimedia.org/wikipedia/commons/8/85/CAMP_2012.jpg', 1)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (2, 'Haight Ashbury Shopping', 2, 'Haight-Ashbury is known for its history of being the origin of hippie subculture. The thrift stores that line the streets are some of the most unique in the city.', 37.769958, -122.446961, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (2, 'Afternoon Coffee at Tartine', 3, 'Organic ingredients provide the makings for breakfast pastries, hot pressed sandwiches & coffee.', 37.761418, -122.424104, 'http://s3-media4.fl.yelpcdn.com/bphoto/SG0NJG1prp5RC11UfshF7Q/o.jpg', 2)")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (3, 'Brunch at Kitchen Story', 1, 'At Kitchen Story, a new restaurant in San Franciscos Castro neighborhood, lunchtime diners come for the bacon—and return for Asian-influenced California cuisine.', 37.764176, -122.430668, 'http://s3-media1.fl.yelpcdn.com/bphoto/ttVmYYSvxAJwINqhDZJZZA/ls.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (3, 'Chinese Historical Society of America Museum', 2, 'Chinatown is cruicial to the history of SF, and you can see that in the rich history of this museum.', 37.793844, -122.408779, 'http://sfbeautiful.org/wp-content/uploads/2014/10/chinese-historical-society_full.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (3, 'Relax at Dolores Park', 3, 'Encompassing nearly 16 acres, Mission Dolores Park is one of SFs most popular parks, the vibrant heart of its culturally diverse neighborhood. Many festivals, performances, and other cultural events are held here, and on sunny afternoons people flock to the park to play, picnic, lounge, and enjoy spectacular views of the citys skyline and beyond.', 37.759773, -122.427063, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg', 4)")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (4, 'Super Long Title Testing Whoo WHat Hpappasjjdasdkfa skdfjsla', 1, 'Headreach fluted decasyllable imminent unputrefiable. ', 37.764176, -122.430668, 'http://si.wsj.net/public/resources/images/SF-AB925_LUNCHB_P_20130109105149.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (4, 'Haight Ashbury Shopping', 2, 'Tailpiece capitalise unnatural unwaned concenter. ', 37.769958, -122.446961, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (4, 'Coit Tower', 3, 'This tower was a donation to the local firemen, and is shaped like a firehose.', 37.802395, -122.405822, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg', 4)")



#Berkeley Tour
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (5, 'Campanile Views', 1, 'See the whole panoramic view of Berkeley from the top of the Campanile tower', 37.761418, -122.424104, 'http://www.berkeleyside.com/wp-content/uploads/2015/03/campanile_view1.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (5, 'Doe Library Reading Room', 2, 'The reading room, or Morrison Library, is one of the most beautiful parts of Doe Library.', 37.872208, -122.259493, 'https://s-media-cache-ak0.pinimg.com/736x/44/c0/6c/44c06c6be4b34436d862f222ac2e9fef.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (5, 'Grab a Coffee at FSM', 3, 'Students get tired studying all day, so make sure you grab a drink and a quick snack at the Free Speech Movement Cafe!', 37.874335, -122.262307, 'http://nickm.com/montfort_rettberg/implementation/2004-08-29/Berkeley_California__Free_Speech_Movement_Cafe_1a.jpg', 4)")


# Testing

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (6, 'Lunchtime fun at Pier 23', 1, 'Everyone knows about Pier 39, but have you heard of the Cafe at Pier 23? The views are spectacular and theres no tourists!', 37.803378, -122.400909, 'https://sfslackers.files.wordpress.com/2011/08/pier-23.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (6, 'Shopping Downtown', 2, 'Westfield is the biggest mall within SF, and the place to go for luxury shopping.', 37.784212, -122.406873, 'https://c1.staticflickr.com/3/2608/3742245799_85129f2aa1.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (6, 'Chinese Historical Society of America Museum', 3, 'Chinatown is cruicial to the history of SF, and you can see that in the rich history of this museum.', 37.793844, -122.408779, 'http://sfbeautiful.org/wp-content/uploads/2014/10/chinese-historical-society_full.jpg', 4)")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (7, 'Japantown', 1, 'Look around Japantown and eat some awesome sushi', 37.785413, -122.429383, 'http://sfrecpark.org/wp-content/uploads/83738-586x286.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (7, 'Chinese Historical Society of America Museum', 2, 'Chinatown is cruicial to the history of SF, and you can see that in the rich history of this museum.', 37.793844, -122.408779, 'http://sfbeautiful.org/wp-content/uploads/2014/10/chinese-historical-society_full.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (7, 'Explore Little Italy', 3, 'The small area of Little Italy is located in the North Beach district, in the northeastern area of the city of San Francisco.', 37.800762, -122.410804, 'https://s-media-cache-ak0.pinimg.com/736x/83/04/83/830483e13b338031a79b8f50c7d43c29.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (7, 'Coit Tower', 4, 'This tower was a donation to the local firemen, and is shaped like a firehose.', 37.802395, -122.405822, 'http://www.destination360.com/north-america/us/california/san-francisco/images/s/coit-tower.jpg', 4)")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (8, 'AT&T Park Walk', 1, 'Home of the Giants!', 37.778595, -122.38927, 'http://www.ballparksofbaseball.com/nl/pictures/2013/att13_top2.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (8, 'Lunch in Soma', 2, 'Some is the heart of tech in SF, and youll see plenty of unicorns walking its streets. Make sure to try the watermelon beer!', 37.789892, -122.390145, 'http://sfbrewersguild.org/wp-content/uploads/2013/02/21st-Amendment-Restaurant.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (8, 'South Park', 3, 'South Park is the citys startup capital, and where most of the citys startups were founded.' , 37.759773, -122.427063, 'http://x.lnimg.com/photo/poster_768/98c63caa55104e23aa096fa3db10e793.jpg', 4)")

#Chicago
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (9, 'Velvet Taco', 1, 'The most creative tacos youve ever tried!', 41.878114, -87.629798, 'http://s3-media3.fl.yelpcdn.com/bphoto/GJgWxFvZh7HjwXd5099oKA/o.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (9, 'Walk Down The Magnificent Mile', 2, 'Chicagos Magnificent Mile is the 13 block stretch of North Michigan Avenue that runs from the banks of the Chicago River to the south, to Oak Street to the north.', 41.894809, -87.624214, 'http://doubletree3.hilton.com/resources/media/dt/CHIMMDT/en_US/img/shared/full_page_image_gallery/main/dh_mile_11_677x380_FitToBoxSmallDimension_Center.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (9, 'Relax at Navy Pier', 3, 'Navy Pier is a not-for-profit originally opened as a shipping and recreational facility in 1916. Located on Lake Michigan, it has served many purposes throughout its rich history and currently encompasses more than fifty acres of parks, gardens', 41.889538, -87.628597, 'http://www.destination360.com/north-america/us/illinois/chicago/images/s/navy-pier.jpg', 4)")

db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (10, 'Art Institute', 2, 'At Kitchen Story, a new restaurant in San Franciscos Castro neighborhood, lunchtime diners come for the bacon—and return for Asian-influenced California cuisine.', 37.764176, -122.430668, 'http://si.wsj.net/public/resources/images/SF-AB925_LUNCHB_P_20130109105149.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (10, 'The Picasso', 3, 'Commissioned in 1963, Picasso worked for two years, combining his style from earlier works and taking parts of original sketches, before he finally presented a 42-inch tall model of what he envisioned for the piece.', 41.884061, -87.630243, 'https://c2.staticflickr.com/6/5061/5736050612_a8f21f1262_b.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (10, 'Edward Kemeys The Lions', 1, 'Looking strong, defiant and majestic, they have stood at their perches since 1893, making them one of the oldest displays of public art in this city.', 41.889538, -87.628597, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (10, 'Dinner at Purple Pig', 4, 'The Purple Pig is a collaboration of Chefs Scott Harris of Mia Francesca, Tony Mantuano of Spiaggia, Jimmy Bannos and Jimmy Bannos Jr. of Heaven on Seven. Featuring housemade charcuterie, cheeses and classic Mediterranean fare plus an extensive yet accessible wine list.', 41.878114, -87.629798, 'https://upload.wikimedia.org/wikipedia/commons/2/2a/Dolores_Park,_San_Francisco_2013-04-13_14-48.jpg', 4)")


db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (11, 'Velvet Taco', 1, 'The most creative tacos youve ever tried!', 41.878114, -87.629798, 'http://s3-media3.fl.yelpcdn.com/bphoto/GJgWxFvZh7HjwXd5099oKA/o.jpg', 2)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (11, 'Walk Down The Magnificent Mile', 2, 'Chicagos Magnificent Mile is the 13 block stretch of North Michigan Avenue that runs from the banks of the Chicago River to the south, to Oak Street to the north.', 41.894809, -87.624214, 'http://doubletree3.hilton.com/resources/media/dt/CHIMMDT/en_US/img/shared/full_page_image_gallery/main/dh_mile_11_677x380_FitToBoxSmallDimension_Center.jpg', 4)")
db.execute("INSERT INTO stops (TourID,Name,TourIndex,Description,Lat,Long,Pic1,Category) VALUES (11, 'Relax at Navy Pier', 3, 'Navy Pier is a not-for-profit originally opened as a shipping and recreational facility in 1916. Located on Lake Michigan, it has served many purposes throughout its rich history and currently encompasses more than fifty acres of parks, gardens', 41.889538, -87.628597, 'http://www.destination360.com/north-america/us/illinois/chicago/images/s/navy-pier.jpg', 4)")







# Comments Table
db.execute("CREATE TABLE comments (id INTEGER PRIMARY KEY, TourID INTEGER, Comment TEXT, Rating INTEGER, Time INTEGER, CommenterID INTEGER);")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'I really loved the street art aspect of this tour, thanks for showing us around!', 5, 201508050109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'I now dream of Tartine morning buns. Thanks so much!', 5, 201508010109, 2)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'Found my new favorite Cafe!', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'Cool tour', 4, 201508020109, 4)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (1, 'Tour felt a little long to me, we just stopped after Haight-Ashbury because the shops werent really our style', 3, 201508030109, 1)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'I really loved the street art aspect of this tour, thanks for showing us around!', 5, 1508050109, 4)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'I now dream of Tartine morning buns. Thanks so much!', 5, 201508010109, 5)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'Found my new favorite Cafe!', 5, 201508040109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (2, 'Cool tour', 4, 201508020109, 3)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'I really loved the street art aspect of this tour, thanks for showing us around!', 5, 201508050109, 2)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'Found my new favorite Cafe!', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (3, 'This was such a cool experience, I really loved getting a true feel for the city life! Thanks so much for showing us your favorite places.', 3, 201508030109, 4)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (4, 'Comments are coool!', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (4, 'I like this tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (4, 'Testing purposes', 3, 201508030109, 4)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (5, 'Love this tour!', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (5, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (5, 'Awesome dude', 3, 201508030109, 4)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (6, 'Yekaterinoslav indecorously naphthalize cryptophyte avitaminosis heteroeciously repack missend pout cyllene notochord. !', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (6, 'Provably reannotate unextorted yup upheaval moultrie bewitchery pyrophotometer.', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (6, 'Tour felt a little long to me, we just stopped after Haight-Ashbury because the shops werent really our style', 3, 201508030109, 4)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (7, 'Buffalo monal textbookish tetrabranchiate bout faunally futureless nectarean', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (7, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (7, 'Kibitz aristomachus inalterability hibernator nonexpeditious. ', 3, 201508030109, 4)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (8, 'Found my new favorite Cafe!', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (8, 'Chequerboard nip galuppi forbearer graecise ungravelly cerebration nationalizing. ', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (8, 'Tour felt a little long to me, we just stopped after Haight-Ashbury because the shops werent really our style', 3, 201508030109, 4)")

db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (9, 'FNonfederal gustative buried gasifiable surat sandfishes aughtlins conformability.', 5, 201508040109, 3)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (9, 'Cool tour', 4, 201508020109, 1)")
db.execute("INSERT INTO comments (TourID,Comment,Rating,Time,CommenterID) VALUES (9, 'Hopsacking unfold wettish istria attemptable. Rosamund uncleft unperfumed microdyne stagehand.', 3, 201508030109, 4)")


db.commit()
