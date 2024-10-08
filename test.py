from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get("/")
async def read_root():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")
    return {"message": "Hello World"}
