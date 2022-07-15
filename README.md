## Api Challenge
This was fun :) building an API in 20 minutes

## Prequisites
- Docker and Docker compose

## Clone the repository
```bash
git clone https://github.com/DanNduati/Api_challenge.git
```
## Running with docker compose
```bash
cd Api_challenge/
docker compose up --build -d
```
Navigate to the `/docs` endpoint to interact with the API interactively
```bash
http://0.0.0.0:8000/docs
```
## Overview
You are provided with a JSON file `[customer.json]` available on this repository that represents an object. You will be in a race with your peers to deliver a working HATEOAS compliant API which allows CRUD operation on that object. 

You may identify and use unique parameters to query the data

## Rules
* You are expected to work on this task unassisted.
* You are allowed to bring your own scaffolding code
* The more cloud native and AWS based the solution is the more points you will score
* You are allowed to use the DB of your choice to back the API
* Implementing a CI/CD pipeline will score extra points but is not mandatory
* The solution should be demostrable on AWS or on your local machine (If you do not manage to deploy it to AWS).
* The more cloud native, secure,cost efficient, performant and reliable the solution is the more points you will score.

## Submission
Send an email to your public repo to DockYard@Safaricom.co.ke

PS: Repository URL: https://github.com/saf-se-summit/api-challenge
