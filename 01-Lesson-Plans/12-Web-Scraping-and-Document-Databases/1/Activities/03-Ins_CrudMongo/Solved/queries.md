# Update, Delete and Drop in MongoDB

* Use the travel_db

```shell
db
use travel_db
```

* Insert two countries in Africa

```shell
db.destinations.insertOne({'country': 'Egypt', 'continent': 'Africa', major_cities: ['Cairo', 'Luxor']})
db.destinations.insertOne({'country': 'Nigeria', 'continent': 'Africa', major_cities: ['Lagos', 'Kano']})
```

* Show how to update data using `db.[COLLECTION_NAME].updateOne()`

```shell
db.destinations.updateOne({"country": "Egypt"}, {$set: {"continent": "Antarctica"}})
```

* Note that the above will only update the first entry it matches.

* To update more than one record, we use the `updateMany` method.

```shell
db.destinations.updateMany({"continent": "Africa"}, {$set: {"continent": "Antarctica"}})
```

* Ask the class what they think will happen when you run this command, even though a capital doesn't exist.

```shell
db.destinations.updateOne({"country": "Morocco"}, {$set: {"capital": "Rabat"}})
```

* Answer: it will add the capital field to the document.

* Show how to push to an array with `$push`.

```shell
db.destinations.update({"country": "Morocco"}, {$push: {"major_cities": "Agadir"}})
```

* The upsert option updates a document if one exists; it otherwise creates a new document.

```shell
db.destinations.updateOne({'country': 'Canada'}, {$set: {'capital': 'Ottawa'}}, {upsert: true})
```

* Show how to delete an entry with `db.[COLLECTION_NAME].deleteOne()`.

```shell
db.destinations.deleteOne({"country": "Morocco"})
```

* Show how to empty a collection with `db.[COLLECTION_NAME].remove()`.

```shell
db.destinations.remove({})
```

* Show how to drop a collection with `db.[COLLECTION_NAME].drop()`.

```shell
db.destinations.drop()
```

* Show how to drop a database

```shell
db.dropDatabase()
```
