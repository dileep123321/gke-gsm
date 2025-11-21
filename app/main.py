from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "GKE Deployment Successful - New App Setup"}

@app.get("/health")
def health():
    return {"status": "healthy"}
 
