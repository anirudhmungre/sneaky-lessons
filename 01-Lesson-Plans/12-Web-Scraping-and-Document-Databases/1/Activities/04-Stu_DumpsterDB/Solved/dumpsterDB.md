# Dumpster Database

* Create and use a database called "Dumpster_DB".


```
use Dumpster_DB
```

* Create the "divers" collection and then insert a couple documents into it


```
db.divers.insertOne({"name":"Davey", "yearsDiving":10, "stillDiving": true, "bestFinds":["Flat Screen", "Ruby Collar", "$100"]})

db.divers.insertOne({"name":"Jeanie", "yearsDiving":1, "stillDiving": true, "bestFinds":["Movie Theater Chairs", "Music Box"]})

db.divers.insertOne({"name":"Boppo", "yearsDiving":5, "stillDiving": true, "bestFinds":["Half-Eaten Hamburger", "Some Goop"]})
```

* Update 'yearsDiving' so that it is one year higher for each diver


```
db.divers.updateOne({"name":"Davey"},{$set:{"yearsDiving":11}})
db.divers.updateOne({"name":"Jeanie"},{$set:{"yearsDiving":2}})
db.divers.updateOne({"name":"Boppo"},{$set:{"yearsDiving":6}})
```

* Update 'stillDiving' to False for Davey


```
db.divers.updateOne({"name":"Davey"},{$set:{"stillDiving": false}})
```

* Add a new value to Jeanie's "bestFinds"


```
db.divers.updateOne({"name":"Jeanie"},{$push:{"bestFinds":"Mona Lisa"}})
```

* Remove Boppo from the collection


```
db.divers.deleteOne({"name":"Boppo"})
```
