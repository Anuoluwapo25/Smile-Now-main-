backend here


## API Endpoints

### /login

**POST** `/login`

#### Description
Authenticate a user and return a token.

#### Request Body
```json
{
  "username": "string",
  "password": "string"
}