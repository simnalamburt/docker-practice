> Working in Progress

docker-practice
========
Docker image with python 2.7.13 + python 3.6.0 + mongodb 3.2. It's based on
Alpine Linux 3.5.

### Instructions
```shell
# Build image
sudo docker build -t docker-practice .

# Run image with psuedo-tty being attached to the screen
sudo docker run -it --rm --name docker-practice docker-practice

# Run image as a daemon
sudo docker run -d --rm --name docker-practice docker-practice
# Attach to the running docker image
sudo docker exec -it docker-practice /bin/sh
# Stop running docker container
sudo docker stop docker-practice
```

###### References
- [Use Supervisor with Docker](https://docs.docker.com/engine/admin/using_supervisord/), by docker team
- [github.com/jbfink/docker-wordpress](https://github.com/jbfink/docker-wordpress), a supervisord sample
- [Supervisor: A Process Control System](http://supervisord.org/), an official webpage
- [Python docker image](https://hub.docker.com/_/python/)
- [Alpine Linux package management - Add a Package](https://wiki.alpinelinux.org/wiki/Alpine_Linux_package_management#Add_a_Package), Alpine Linux wiki
- [`mongodb` package of Alpine Linux](https://pkgs.alpinelinux.org/package/edge/testing/x86_64/mongodb)
- [Dockerize MongoDB](https://docs.docker.com/engine/examples/mongodb/), by docker team

### Why would you do this? Why don't you just separate them into different containers?
![A picture of widowmaker from Overwatch Animated Shrot, "Alive"](http://images.akamai.steamusercontent.com/ugc/268348980135500926/EDF216DBB95088C86BD10D01B666E9BD7429D6B0/)

*(laughs)*

<br>

--------
*docker-practice* is primarily distributed under the terms of both the [MIT license]
and the [Apache License (Version 2.0)]. See [COPYRIGHT] for details.

[MIT license]: LICENSE-MIT
[Apache License (Version 2.0)]: LICENSE-APACHE
[COPYRIGHT]: COPYRIGHT
