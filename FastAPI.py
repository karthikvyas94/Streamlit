from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/",response_class=HTMLResponse)
def read_root():
    return """<!DOCTYPE html>
    <html lang="en">
    <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hello</title>
   </head>
   <body>
  <h1>Hello, welcome to Chat boat</h1>
   </body>
    </html>
    """

@app.get("/cls")
def read_cls():
    return {"message": "Hello from the cls endpoint CArthik b!"}