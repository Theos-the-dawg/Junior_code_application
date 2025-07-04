from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/sort-characters")
async def sort_string(request: Request):
    try:
        payload = await request.json()
        data = payload.get("data")
        if not isinstance(data, str):
            return JSONResponse(content={"error": "Field 'data' must be a string"}, status_code=400)

        sorted_chars = sorted(list(data))
        return JSONResponse(content={"word": sorted_chars}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)