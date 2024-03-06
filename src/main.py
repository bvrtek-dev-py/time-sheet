import uvicorn
from fastapi import FastAPI

from time_sheet.src.infrastructure.ports.api.user.routers import router as user_router
from time_sheet.src.infrastructure.ports.api.project.routers import router as project_router

app = FastAPI()
app.include_router(user_router)
app.include_router(project_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
