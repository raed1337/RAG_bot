# main.py

from fastapi import FastAPI

from routers import query_routers

app = FastAPI()

# Include the router
app.include_router(query_routers.router, prefix="/api", tags=["query"])

# Run the app with Uvicorn if this file is the main entry point
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
