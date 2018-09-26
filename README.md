# crispy-journey
Password Generation Service

This service will generate a random password that's easier to remember and type but still secure. Simple `GET` requests 
with no API key will return a random password following the default format specified below. Requests with an API key
will allow the end user to store, retrieve, or update their passwords for a site.

## Design

### Suggested Architecture

![infrastructure](docs/infrastructure.dot.png)

- Lambda
- S3
- API Gateway
- Github
- Build Service
- Proxy Service

### Project Structure

docs/ - Documentation and design docs
com/zmcneilly/password/ - Code to be run in Lambda
