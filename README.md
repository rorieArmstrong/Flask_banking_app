# Software engineer - assignment

The goal is to write a web app, using flask, to display money ovement data to internal op. staff.

The scope of the task is not limited to the acceptance criteria and you may ipt to over-engineer certain parts to show off experise or concepts you think would be advantageous.

Having realistic data is not required, so feel free to mock data.

# Aceptance criteria

## 1. A login functionallity
- user can be mocked, registration is out of scope.
- should display logged in users name.
- should redirect to login if not logged in.

## 2. Money movements
- a list to view money movements.
- a money movement item has a date, currency, amount, sender and a link to show more details.

## 3. Details view
- the details view can be reached by click a coponent in movements view.
- the details are at least what is displayed in 2
- A reciever is shown
- a text input exists to create notes

## 4. General 
- App should be startable on Ubuntu 20.04 LTS
- Any packing/dependancies can be used as long as install instructions exist

# Build

## Required packages

- flask
- flask-login
- flask-sqlalchemy

please install with pip install (if not alread present)

The app can then be ran using main.py and will be runing on port 8000

You can then create an account and view the mocked data