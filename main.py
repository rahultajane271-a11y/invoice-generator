from fastapi import FastAPI, UploadFile, File
import shutil
from parser import parse_invoice
app = FastAPI()

@app.post("/upload")
async def upload_invoice(file: UploadFile = File(...)):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    data = parse_invoice(path)

    return data