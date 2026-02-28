from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.get("/info")
def get_info():
    """Endpoint returning a JSON object with 'name' and 'description'."""
    return {
        "name": "Simple API",
        "description": "A simple REST API built using FastAPI."
    }