all: thrift client
	./gradlew build

thrift:
	@if [ ! -d "src/main/java/thrift" ]; then \
		thrift --gen java ../lucidaservice.thrift; \
		thrift --gen java ../lucidatypes.thrift; \
		sed -i '1s/^/package thrift;\n/' gen-java/LucidaService.java; \
		sed -i '1s/^/package thrift;\n/' gen-java/QueryInput.java; \
		sed -i '1s/^/package thrift;\n/' gen-java/QuerySpec.java; \
		mkdir src/main/java/thrift/; \
		mv gen-java/* src/main/java/thrift/; \
		rmdir gen-java/; \
    fi

client:
	cd TemplateClient/ && ./compile-Template-client.sh

start_server: 
	gnome-terminal -x bash -c "./gradlew run $(filter-out $@,$(MAKECMDGOALS)); read -n1"

start_test: 
	gnome-terminal -x bash -c "cd TemplateClient; ./start-Template-client.sh $(filter-out $@,$(MAKECMDGOALS)); read -n1"

clean:
	rm -rf src/main/java/thrift ; \
	rm -rf TemplateClient/thrift ; \
	rm -rf TemplateClient/*.class ; \
	rm -rf build;

.PHONY:	all thrift gradle start_server start_test clean

%:
	@:
