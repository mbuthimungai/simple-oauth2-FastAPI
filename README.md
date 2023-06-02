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

## How to implement
* This is a example implementation
```python
from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
```
