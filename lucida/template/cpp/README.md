# Template microservice in C++

This is a template of microservice built in lucida. To build your own service, follow the steps below.

## Major Dependencies

- [Facebook Thrift](https://github.com/facebook/fbthrift)

# Structure

- `server/`: implementation of the template server
- `test/`: implementation of the template testing client

### Step 0: move the directory 

To get started, place the directory under `lucida/lucida` folder, and change the name of your directory into a specified name represent your service.

### Step1: change the configuration

Change the port number for your service (default is 8889) in [server/TemplateServer.cpp](server/TemplateServer.cpp).

### Step2: implement your own create/learn/infer methods

Implement your own create/learn/infer methods in [server/TemplateHandler.cpp](server/TemplateHandler.cpp). The spec of these three function is in the toppest-level readme. Your are free to import different packages for your service, but remember to add the dependence correctly.

### Step3: update the `Makefile`

Update the [Makefile](Makefile). The default one has included the generating Thrift stubs code. You only need to add the dependence of your own service.

### Step4: test your service individually

Change the [test application](test) corresponding to your service. After that, do the following steps under this directory to test your service. Remember to change the test query to make sure your service works.

- build 

 ```
 make all
 ```

- start server

 ```
 make start_server
 ```
- start testing

 ```
 make start_test
 ```

### Step5: insert your service into Lucida

Modify the top-level `Makefile` and `lucida/Makefile` so that `make local` and `make start_all` include your service.

