all: thrift

thrift:
	@if [ ! -d "lucidaservice" ]; then \
        thrift --gen py ../lucidaservice.thrift; \
        thrift --gen py ../lucidatypes.thrift; \
        cd gen-py; \
        mv * ..; \
        cd ..; \
        rmdir gen-py; \
        rm __init__.py; \
    fi

clean:
	rm -rf lucidaservice lucidatypes ; \
	rm -rf *.pyc; 

start_server:
	gnome-terminal -x bash -c "cd server; python server.py $(filter-out $@,$(MAKECMDGOALS)); read -n1"

start_test:
	gnome-terminal -x bash -c "cd client; python client.py $(filter-out $@,$(MAKECMDGOALS)); read -n1"
