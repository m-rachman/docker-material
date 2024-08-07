# DOCKER NOTES

---
# A. Installation
- Main source : https://docs.docker.com/desktop/
- Please install based on the specifications of the computer you are using.
- If the computer version you are using does not meet the minimum requirements from the official source, you can still install docker with Docker Toolbox. 
- For more information about Docker Toolbox, please read [source 1](https://www.upwork.com/resources/docker-toolbox) and [source 2](https://nickjanetakis.com/blog/should-you-use-the-docker-toolbox-or-docker-for-mac-windows).
- To verify installation, open Commnd Prompt or Terminal, and type `docker`. If the installation is successful, a list of Docker commands will appear.

---
# B. Tutorial
You can use some of the sources below to learn more about Docker :
1. [Docker 101 Tutorial](https://www.docker.com/101-tutorial/)
   
2. [Docker-curriculum.com](https://docker-curriculum.com/)

---
# C. Syntax
## C.1 - Basic Syntax
1. Get list of Docker command
   ```
   $ docker
   ```

2. Check Docker version
   ```
   $ docker --version
   ```

## C.2 - Try it out
Use the following instructions to run a container.

3. Open Docker Desktop and select the Search field on the top navigation bar.

4. Specify welcome-to-docker in the search input and then select the Pull button, or go to the GitHub repository using this [link](https://github.com/docker/welcome-to-docker).
5. Once the image is successfully pulled, select the Run button.

6. Expand the Optional settings.

7. In the Container name, specify welcome-to-docker.

8. In the Host port, specify 8080. 

## C.3 - Docker Image
10. Build a Docker Image from Dockerfile
   ```
   Syntax  : $ docker build -t <app-name>:<tag> .
   
   Example : $ docker build -t my-game:v0.0.1 .
   ```

11. Change tag of a Docker Image
   ```
   Syntax  : $ docker tag <app-name>:<old-tag> <app-name>:<new-tag>

   Example : $ docker tag my-game:v0.0.1 my-game:v0.0.2
   ```

12. Run a Docker Image
   ```
   Syntax  : $ docker run [options] <app-name>:<tag>
   Example : $ docker run -it my-game:v0.0.1
   ```
   For more details about `docker run` or `[options]`, please visit [the official documentation](https://docs.docker.com/engine/reference/run/).

13. List all Docker Images
   ```
   Syntax : $ docker images
   ```

## C.3 - Docker Container


14. List all Docker Container
   ```
   Syntax : $ docker ps -a
   ```
---
# D. Push to DockerHub
1. Login to DockerHub
   ```
   Syntax : $ docker login
   ```

2. Create tag between image that you want to push and repository in DockerHub
   ```
   Syntax  : $ docker tag <image-id> <dockerhub-username/image-name/tag>
   Example : $ docker tag afa783ad460f rhmndocker/my-game:v0.0.1
   ```
   
3. Push to Docker Hub
   ```
   Syntax  : $ docker push <dockerhub-username/image-name/tag>
   Example : $ docker push rhmndocker/my-game:v0.0.1
   ```

4. If you experience an error like the following :
   ```
   denied: requested access to the resource is denied
   ```
   
   log out first with the syntax below then repeat step 1 to step 3
   ```
   Syntax : $ docker logout
   ```
5. go to your dockerhub account and find the images

6. To test the image that has been pushed
   *Make sure that on your computer there are no more images that are the same as the image you just pushed*
   ```
   Syntax  : $ docker run [options] <dockerhub-username/image-name/tag>
   Example : $ docker run -it rhmndocker/my-game:v0.0.1
   ```
## D.1 Docker Buildx
   To build and push a multi-architecture image using Docker Buildx, you would:
   
7. Create a New Buildx Builder (if not already set up):
   ```
   docker buildx create --use
   ```

8. Build for Multiple Architectures:
   ```
   docker buildx build --platform linux/amd64,linux/arm64 -t rhmndocker/my-game:v123 --push .

   ```
