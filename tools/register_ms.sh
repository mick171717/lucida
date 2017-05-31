#!/bin/bash

python service_mongo.py questionanswering QA localhost 8082 text\&text_image
python service_mongo.py imagematching IMM localhost 8083 image\&text_image
python service_mongo.py calendar CA localhost 8084 text
python service_mongo.py imageclassification IMC localhost 8085 image\&text_image
python service_mongo.py facerecognition FACE localhost 8086 image\&text_image
python service_mongo.py digitrecognition DIG localhost 8087 image\&text_image
python service_mongo.py weather WE localhost 8088 text
python service_mongo.py musicservice MS localhost 8089 text
