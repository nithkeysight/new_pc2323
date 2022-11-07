#main.py
import fastapi
import uvicorn

print("Hello")

api = fastapi.FastAPI()

@api.get("/api/endpoint")
def endpoint():
    return {"msg":"Hello fast api"}

uvicorn.run(api, port=9000)
