# Project Name
> Recruitment task - backend internship 2022

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [TO DO](#to-do)
* [Contact](#contact)


## General Information
This application performs some operations on emails and logs files, and show results for user. This is a task for an internship in IT company. Application created and tested on Ubuntu 20.04.

## Technologies Used
* Python 3.10.4
* Pandas 1.4.2
* Pytest 7.1.2
* Docker

## Features

* The program prints the number of invalid emails, then one invalid email per line.
* The program takes a string argument and print the number of found emails, then prints one found email per line.
* The program groups emails by one domain and order domains and emails alphabetically.
* The program finds emails that are not in the provided logs file and prints the numbers of found emails, then one found email per line sorted alphabetically.

## Setup:

### Docker:
#### In the beginning, you have to install Docker on your PC.
* [Here is a link](https://docs.docker.com/engine/install/ubuntu/) explaining how to install Docker on Ubuntu.

#### You will have to pull an image of the app:
* `docker pull dar2kov/interapp:latest` 

### Virtual environment:
#### In the beginning, you have to clone the repository from GitHub to your PC.
* [Here is a link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) explaining how to clone repository.

#### If you want to use this application, you will need to install packages from requirements.txt file to a virtual environment. 
* [Here is a link](https://www.arubacloud.com/tutorial/how-to-create-a-python-virtual-environment-on-ubuntu.aspx) explaining how to create virtual environment on Ubuntu.
* [Here is a link](https://stackoverflow.com/questions/7225900/how-can-i-install-packages-using-pip-according-to-the-requirements-txt-file-from) explaining how to install packages from requirements.txt.

## Usage

### Docker:
* Type `docker run dar2kov/interapp` to print help.
* `docker run dar2kov/interapp -ic, --incorrect-emails`
* `docker run dar2kov/interapp -s PHRASE; --search PHRASE`
* `docker run dar2kov/interapp -gbd; --group-by-domain`
* `docker run dar2kov/interapp -feil PATH_TO_LOGS_FILE; --find-emails-not-in-logs PATH_TO_LOGS_FILE`\
There is set a default path to a logs file, but you can add your own path manually.

### Virtual environment:
If you want to use this application, write a command from the examples below:
* `python main.py -h`
* `python main.py -ic; --incorrect-emails`
* `python main.py -s; PHRASE; --search PHRASE`
* `python main.py -gbd; --group-by-domain`
* `python main.py -feil PATH_TO_LOGS_FILE; --find-emails-not-in-logs PATH_TO_LOGS_FILE`\
There is set a default path to a logs file, but you can add your own path manually.

## Project Status
* The main features are done, but I have some ideas, and it's a great practise exercise.

## To do:
* I want to complete writing unit tests.. (current ~90%)
* I want to create a docstring for each class...


## Contact
* #### Created by Dariusz Kowalczyk - dariusz_kowalczykk@wp.pl - feel free to contact me!
