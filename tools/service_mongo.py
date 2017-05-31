from pymongo import *
import sys, os

if len(sys.argv) != 6 :
	print('error: wrong number of argument.')
	exit(-1)

mongodb_addr = os.environ.get('MONGO_PORT_27017_TCP_ADDR')
if mongodb_addr:
	print('MongoDB: ' + mongodb_addr)
	db = MongoClient(mongodb_addr, 27017).lucida
else:
	print('MongoDb: localhost')
	db = MongoClient().lucida

collection = db.service_info

result = collection.count({"name" : sys.argv[1]})
if result != 0:
	collection.delete_many({"name" : sys.argv[1]})

# list the attributes for the interface
post = {
	"name" : sys.argv[1],
	"acronym" : sys.argv[2],
	"host" : sys.argv[3],
	"port" : sys.argv[4],
	"input" : sys.argv[5] 
}

post_id = collection.insert_one(post).inserted_id
exit(0)
