from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/notify")
async def notify(request: Request):
    data = await request.json()
    # BEGINNER: Edit this secret to your actual secret from Google Form!
    YOUR_SECRET = "7702826245"
    if data.get("secret") != YOUR_SECRET:
        return JSONResponse(content={"status": "Unauthorized"}, status_code=401)
    # Print or log the received data for debugging
    print("Received POST:", data)
    return JSONResponse(content={"status": "ok"}, status_code=200)
