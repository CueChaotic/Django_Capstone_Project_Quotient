# PROJECT QUOTIENT

## A brief introduction

Put simply, Project Quotient is an idea for a website of a game developer. It's a core part of my
journey to learn and develop skills in Software Engineering. It is, at this point, intended to be
entirely theoretical and in no way represents a real company or commercial undertaking (even the
name is a placeholder).

BUT, that being said, who knows what the future holds?

## Contents
1. Feature Overview
2. Installation
3. Usage
4. Credits

## 1. Feature overview

The current build has the following features built using Django:
* Landing page, with a brief introduction to the "company".
* Functional new user registration.
* Functional user login and authentication (Username and Password).
* Functional forum where users may post new discussion topics and add commentary to existing topics.
* A non-functional store page.
* Working links to all of the above.

NOTE: All the imagery is AI-generated (including the logo), massive thanks to ChatGPT for all its
hard work in that respect, you made me proud.

## 2. Installation

   ### 2.1 Building the site and just running the build in a virtual environment
   
      2.1.1 Open the Command Terminal relevant to your operating system and navigate to the directory
            you would like to use for the project files.

      2.1.2 Clone this Git repository to your chosen local directory by running this command in your
            terminal:
            ```
            git clone https://github.com/CueChaotic/Django_Capstone_Project_Quotient.git
            ```

      2.1.3 A new directory called Django_Capstone_Project_Quotient should now appear within your
            current directory. Navigate into this new folder in your terminal.

      2.1.4 While in Django_Capstone_Project_Quotient, run the following command in your terminal:
            > pip install -r requirements.txt
            This will check for, download and install the programs required to build the site.

      2.1.5 Next, we will create a virtual environment which will typically be used when building the
            website. Make sure you are still in the parent directory of the project (being
            Django_Capstone_Project_Quotient). Then run the following command in your terminal:
            > python -m venv myenv
            This will create a Virtual Environment called "myenv" but you can name this environment
            whatever you prefer.

      2.1.6 Activate the Virtual Environment:
            * In Windows run: myenv\Scripts\activate
            * In Mac/Linux, run: source myenv/bin/activate

      2.1.7 Run the following command to complete migrations (needed to run the Forum functionality):
            > python manage.py migrate

      2.1.8 To run the site in Django, run the following command:
            > python manage.py runserver
            This will give you a link to the site that can be opened in your web browser.
            VOILA! You should now be able to browse the site.
            To shut the local server in your terminal, press Control + C.

      2.1.9 Deactivate your Virtual Environment by running:
            > deactivate
      
   ### 2.2 Running the site with a Docker image

      2.2.1 Complete steps 1 through 9 in 2.1 above.

      2.2.2 Create an account (if you don't have one already) on Docker here:
            > https://app.docker.com/

      2.2.3 Download the Docker Desktop App and install it. Ensure it is up and running in the
            background.

      2.2.4 In your terminal, ensure you are in the parent (root) directory of the website project,
            namely: Django_Capstone_Project_Quotient

      2.2.5 Run the below command to check that your Docker is working as intended:
            > docker run hello-world
            There should be a success message.

      2.2.6 In the root directory, you will see a Dockerfile (no extension). This Dockerfile is
            used to give instructions to Docker as to how and what to run when all the files are
            held in a Docker image.

      2.2.7 Run the following command to create a Docker image from the project files:
            > docker build -t project_site ./
            "project_site" is the name of the docker image we're creating. You may use any name you
            wish however.

      2.2.8 Run the following command to run the image container:
            > docker run -p 8000:8000 project_site
            There will be an http://localhost link that you can use to open the site in a web browser.
            VOILA! You should now be able to browse the site.

      2.2.9 To use the terminal again, press Ctrl + C 3 times to force exit.

      2.2.10 Run the below command to list active containers:
            > docker ps
            Take note of the container ID.

      2.2.11 Run the below command to stop the container.
            > docker stop <container ID>
            Replace <container ID> with the actual container ID you want to stop.

   ### 2.3 Pushing an image to your online Docker Hub repository

      2.3.1 Complete steps 1 through 11 in 2.2 above.

      2.3.2 Log in to the Docker website, navigate to Docker Hub, then navigate to the Repositories
            tab.

      2.3.3 Select the "Create a repository" button. Give the repository a name, such as project_site in
            this case.

      2.3.4 You will need to rename your local image file to be consistent with the online repository.
            To do so, run the below command:
            > docker tag project_site <your Docker username>/project_site
            This changes the name of the image from project_site to <your Docker username>/project_site

      2.3.5 You will need to login to Docker from your terminal before you can push to your online repo:
            Run the command below:
            > docker login
            You will be prompted to input your login details.

      2.3.6 Finally, you can now upload (i.e. "push") your image to your Docker Hub repo:
            > docker push <your Docker username>/project_site
            Check the above repo in Docker Hub and the image should be there once finished uploading!

   ### 2.4 Pulling an existing image from a Docker repo

      2.4.1 You can also pull a Docker image from an existing repo. To see an example of an image
            completed and uploaded from the process above, navigate to:
            https://hub.docker.com/r/cuechaotic/project_site

      2.4.2 Run the Docker login command again in your terminal and input your login details as
            prompted.

      2.4.3 You will see a docker pull command in the above repo that you can copy and paste into your
            terminal. Do so and run the command:
            docker pull cuechaotic/project_site

      2.4.4 Run the Docker and see what the site should look like!
            > docker run -p 8000:8000 cuechaotic/project_site
            Now try this with the image in your own repository.

## 3. Usage

This build for the Project/Quotient website can be rendered using any browser. The below desktop
browsers are recommended:
* Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari
* Opera
* Opera GX

Handheld apps: The current build is **not** yet recommended for viewing on Android or Apple
handheld devices.

## 4. Credits

Build entirely done by Patrick Hammond a.k.a. CueChaotic
