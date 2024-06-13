# urine_strip_analysis

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Running the Application](#running-the-application)
4. [Usage](#usage)
5. [API Documentation](#api-documentation)
6. [Contributing](#contributing)

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)

## Setup

#### `Clone the repository:`

```bash
   git clone https://github.com/itechdivyanshu/urine_strip_analysis.git
   cd urine_strip_analysis
```

#### `Create and activate a virtual environment:`

```bash
python -m venv env
source env/bin/activate
```

#### `Install dependencies:`

```bash
pip install -r requirements.txt
```

#### `Run migrations:`

```bash
Copy code
python manage.py migrate
```

## Running the Application

```bash
python manage.py runserver
```

## Usage

Navigate to http://127.0.0.1:8000/ in your browser.
Upload an image of the urine strip to get the RGB values of the colors.

## API Documentation

### Upload Image
* URL: /api/upload/
* Method: POST
* Payload:

```json
{
  "image": "file"
}
```

* Response:

```json
{
  "URO": [206, 193, 187],
  "BIL": [202, 185, 164],
  ...
}
```

## Contributing

If you'd like to contribute to this project, please follow these steps:

```
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
```
