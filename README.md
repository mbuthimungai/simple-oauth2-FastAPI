# simple-oauth2-FastAPI
This is a Fast API application which depicts usage of Oauth2

## What is oauth2
  This is a specification that handles authorization and authentication.
  It is an example of waht systems with "login with google or login with facebook".
  
  In Oauth2 the several ways to handle security are called `flows`.
  The various kinds of flows include:
  * implicit
  * clientCredentials
  * authorizationCode
  * password\
 In this application I have implemented the `password flow`.

# Requirements, Packages used and Installation

Download and install [python](https://www.python.org/downloads/). Be sure to check the checkbox add python to path.

## Installation 
Navigate to your projec directory for this case will be simple-oauth2-FastAPI.

### 1. Clone repository to your local machine
`git clone https://github.com/mbuthi/simple-oauth2-FastAPI`

### 2. Create an environment
> Check to make sure you are in the same directory where you did the git clone,if not navigate to that specific directory.

Depending on your operating system, make a virtual env to prevent messing with your system's primary dependencies

### Windows
`
cd simple-oauth2-FastAPI
py -3 -m venv venv
`

### macOS/Linux
`
cd simple-oauth2-FastAPI
python3 -m venv venv
`

### 3. Activate environment

### Windows
`
venv\Scripts\activate
`

### macOs/Linux
`
source venv/bin/activate
`

### 4. Install the requirements
`pip install -r requirements.txt`

### 5. Run the application
`uvicorn main:app --reload`
