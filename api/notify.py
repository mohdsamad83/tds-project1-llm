import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/notify")
async def notify(request: Request):
    data = await request.json()
    YOUR_SECRET = "7702826245"
    if data.get("secret") != YOUR_SECRET:
        return JSONResponse(content={"status": "Unauthorized"}, status_code=401)
    print("Received POST:", data)
    # Try to save to a file (may not persist on Vercel, but good for local/dev)
    try:
        with open("last_request.json", "w") as f:
            json.dump(data, f)
    except Exception as e:
        print("Error writing JSON file:", e)
    return JSONResponse(content={"status": "ok"}, status_code=200)
