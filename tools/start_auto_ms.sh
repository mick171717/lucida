#!/bin/bash

echo "============================================="
echo "     Lucida Micro Service Building Tools     "
echo "          made in May 31, 2017"
echo "============================================="
echo ""

echo "Specify your service name (e.g. musicservice)."
printf "### Enter your service name: "
read NAME

echo ""
echo "Specify the acronym of your service (e.g. MS)."
printf "### Enter the acronym of your service: "
read NAME_ACN

echo ""
echo "Specify the programming language you want to you in your programming. If C++/Java/Python, then template will be provided."
printf "### Enter the programming language: "
read LAN

echo ""
echo "Specify the host/port information. "
printf "### Enter the host: "
read HOST
printf "### Enter the port: "
read PORT

echo ""
echo "Specify the input type of your service (text, image or text_image)"
printf "### Enter the input type: "
read INPUT

python service_mongo.py $NAME $NAME_ACN $HOST $PORT $INPUT

if [ "$LAN" = "C++" -o "$LAN" = "cpp" ]
then
	# do copy template folder of cpp to lucida
	cd ../lucida ; \
	if [ -d $NAME ]
	then
		echo "[Error] service already exists!"
	else
		cp -rf template/cpp .
		mv cpp $NAME
		echo "[Info] Template folder is ready cpp!"
	fi
elif [ "$LAN" = "Java" -o "$LAN" = "java" ]
then
	# do copy template folder of java to lucida
	echo "Template folder is ready!"
elif [ "$LAN" = "Python" -o "$LAN" = "python" ]
then
	# do copy template folder of python to lucida
	echo "Template folder is ready!"
else
	# create an empty folder
	cd ../lucida ; \
	if [ -d $NAME ]
	then
		echo "[Error] service already exists!"
	else
		mkdir $NAME
		echo "[Info] Template folder is ready!"
	fi
fi

