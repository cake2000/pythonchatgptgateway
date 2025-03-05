# pythonchatgptgateway

A simple example for running a python server that serves as a gateway between clients and ChatGPT server.

# Instructions to run server

## Step 1

Rent a new cloud server, such as a droplet from DigitalOcean. log into that server remotely.

## Step 2

pip install fastapi pydantic openai uvicorn

## Step 3

get your API key from OpenAI and put it in the server.py file in line 11

## Step 4

python3 server.py

# Instructions to run client

## Step 1

get the server IP address, and replace "localhost" in line 25 of client.py with the actual server IP

## Step 2

python3 client.py
