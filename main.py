from fastapi import FastAPI

app = FastAPI(title="TestApp")

@app.get('/items')
async def list_items():
    return []

@app.get('/')
async def root():
    return {"message": "Welcome to the TestApp!"}

@app.get('/api/health')
async def health_check():
    return {"status": "ok"}
