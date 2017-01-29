> Working in Progress

docker-practice
========
Docker image with both python 3.5 and mongodb 3.2.

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
- https://docs.docker.com/engine/admin/using_supervisord/
- https://github.com/jbfink/docker-wordpress
- http://supervisord.org/
- https://hub.docker.com/_/python/
- https://hub.docker.com/_/mongo/
- https://docs.docker.com/engine/examples/mongodb/

### Why would you do this? Why don't you separate those two to different containers?
![A picture of widowmaker from Overwatch Animated Shrot, "Alive"](http://images.akamai.steamusercontent.com/ugc/268348980135500926/EDF216DBB95088C86BD10D01B666E9BD7429D6B0/)

*(laughs)*

--------

`(APACHE-2.0 OR MIT)`
