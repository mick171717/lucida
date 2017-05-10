all:
	cd server ; \
	make all ; \
	cd ../test; \
	make all ; \
	cd ..;

start_server: 
	gnome-terminal -x bash -c "cd server; ./template_server $(filter-out $@,$(MAKECMDGOALS)); read -n1"

start_test: 
	gnome-terminal -x bash -c "cd test; ./template_test $(filter-out $@,$(MAKECMDGOALS)); read -n1"

clean:
	cd server ; \
	make clean ; \
	cd ../test; \
	make clean ; \
	cd ..;

docker:
	cp ../lucidaservice.thrift .; \
	cp ../lucidatypes.thrift .; \
	cp ../../Makefile.common .; \
	docker build -t lucida_template .; \
	rm lucidaservice.thrift; \
	rm lucidatypes.thrift; \
	rm Makefile.common;

%:
	@:
