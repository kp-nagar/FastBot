from fastapi import FastAPI, Request, UploadFile, File
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from util.logger import logger
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil


# from src.api.core.chat_bot

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    logger.info(f"loading index page.")
    try:
        return templates.TemplateResponse("index.html", {"request": request})
    except Exception as e:
        print(e)


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(None)):
    try:
        logger.info(f"saving file: {file.filename}")
        with open(file.filename, 'wb') as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"saved file: {file.filename}")
        return {'filename': file.filename}
    finally:
        file.file.close()