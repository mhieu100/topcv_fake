# File Upload API

A simple Python Flask API that receives file uploads via HTTP POST requests and saves them to the server.

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```

The server will start at http://localhost:5000

## API Endpoints

### POST /upload

Accepts file uploads and saves them to the `uploads` folder.

#### Example using curl:

```bash
curl -X POST -F "file=@/path/to/your/file.txt" http://localhost:5000/upload
```

#### Example using HTML form:

```html
<form action="http://localhost:5000/upload" method="POST" enctype="multipart/form-data">
  <input type="file" name="file">
  <input type="submit" value="Upload">
</form>
```

## Response

The API returns a JSON response with information about the uploaded file:

```json
{
  "message": "File uploaded successfully",
  "filename": "example.txt",
  "path": "uploads/example.txt"
}
``` 