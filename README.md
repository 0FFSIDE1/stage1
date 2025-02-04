# HNG 12 Stage One
Description: This project is to return interesting maths facts about a number


## Setup

1. Clone the repo.
 ```sh
 git clone "<repo_url>"
```

2. Create a virtual environment.
 ```bash
    python3 -m venv .venv
 ```

3. Activate virtual environment.
```bash
    source /path/to/venv/bin/activate`
```

4. Install project dependencies `pip install -r requirements.txt`

5. Create your own branch.
 ```sh
 git branch <branch-name>
```

6. Pull from origin/main branch.
 ```sh
 git fetch origin main
 git merge origin/main

```

7. Make makemigrations.
 ```sh
 python manage.py makemigrations
```

8. Migrate.
 ```sh
 python manage.py migrate
```

9. Runserver.
 ```sh
 python manage.py runserver
```


# API Documentation

## Overview
The `RandomMathFacts` API provides random facts, and interesting properties of a provided number.

## Base URL
http://127.0.0.1:8000

## Endpoints

### 1. Get number properties
**Endpoint: GET /api/classify-number?number=6**  

**Description:**  
Get random facts and properties:
- number
- is_prime
- is_perfect
- properties
- digit_sum
- fun_fact

**Response Format:**
- **Status Code:** `200 OK`
- **Content-Type:** `application/json`

#### Example Request
```bash
curl -X GET http://127.0.0.1:8000/api/classify-number?number=6
```












