###########################
### Migration to Podman ###
###########################

# Build the container image
podman stop iconito-app
# Remove all containers
podman rm $(podman ps -a -f status=exited -q)
# Remove all images 
podman rmi $(podman images -a -q)
podman build -t iconitodev .

# Run container interactive modee
# http://localhost:8080
# podman run -it -p 8080:5000 iconitodev /bin/bash

# Run the container image in localhost
# http://localhost:8080
#podman run -d -p 8080:5000 --name iconito-app iconitodev
podman run -d -p 8080:8080 --name iconito-app iconitodev
#podman run -it -p 8080:8080 --name iconito-app iconitodev