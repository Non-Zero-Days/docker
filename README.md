## vs-code

### Prerequisites:

Install [Docker Desktop](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
    - Note that this is the most environmentally complex pre-req we've used so far in this course. If you need to spend your non-zero day on setting this up that's fully appropriate. We will be using Windows 10 Professional for the demonstrated environment.

Install [Visual Studio Code](https://code.visualstudio.com/)


### Loose Agenda:

Play with Docker
Create container images


### Step by Step

#### Setup playground

Create a directory for playing
Open a powershell terminal to the relevant directory


#### Pull an image from Docker Hub

```
docker pull alpine
```

Review images on local system

```
docker images -a
```


#### Run an image

Let's run the container image
```
docker run alpine
```

Note that nothing happened. Let's check the running containers
```
docker ps -a
```

Let's clean up our environment and try that again
```
docker rm $(docker ps -aq)
docker run -it alpine
```

the ```-it``` argument tell docker that you want to attach to the container process that's starting up. Read more on the arguments we'll be using in [Docker Documentation](#Documentation). You should now see the following which indicates you're attached to an Alpine linux distribution environment.
```
/ #
```

Try running some linux commands

```
ls
```

```
top
```

CTRL+C to exit the top process then type ```exit``` to exit the container. Note that we now need to clean up the container as it is left in a stopped state.

See the containers
```
docker ps -a
```

Clean up
```
docker rm $(docker ps -aq)
```

Going forward we will use ```--rm``` to tell Docker to clean up the container on exit.


#### Create Dockerfile

Open Visual Studio Code to our directory for today's exercise. 

Create a new file named ```Dockerfile``` and open it for edit.

Enter the following
```
FROM alpine

```

Now let's navigate back to our terminal instance. Verify that our terminal is in the same directory that our dockerfile is in.

Note the [Docker Documentation](#Documentation) section contains Dockerfile insights.


#### Run a Dockerfile

Run
```
docker build -t non-zero-image .

```

This will build our image and tag it as ```non-zero-image```. Verify with the ```docker images``` command.

Now let's run the image as before but with our new tag.
```
docker run -it --rm non-zero-image

```

We can now iterate on our Dockerfile and rebuild it.  


#### Revisit Previous Exercise with Docker

Let's grab the code from our [Python Flask exercise](https://github.com/Non-Zero-Days/basic-flask) and create a Dockerfile for it.

If you don't readily have the app.py and motd.txt then go ahead and clone it to another directory. For today's exercise we will simply drag those files into our new play directory, though it would be equally viable to store the Dockerfile we're making in that repository.

Once we've added motd.txt and app.py to today's directory, let's adjust the final line of the app.py file

Change
```
app.run()
```

to

```
app.run(host="0.0.0.0")
```

Now let's adjust our Dockerfile as follows
```
FROM python:3.9.1-alpine
ADD . /code
WORKDIR /code
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

```

We've changed the base image to one which has python already installed, then we've pulled our code into the image, installed our prerequisites (flask) and indicated that we want to run app.py as the startup activity. Let's build and run the image.

```
docker build -t non-zero-image .
docker run -it --rm -p 5050:5000 non-zero-image

```

Open your internet browser of choice and navigate to ```localhost:5050/motd```

You should see ```Happy Non-Zero Month!```

Congrats on your Non-Zero day!


### Documentation
- [Docker Run](https://docs.docker.com/engine/reference/commandline/run/)
- [Dockerfile](https://docs.docker.com/engine/reference/builder/)
