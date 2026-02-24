from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
from PIL import Image
import io

app = FastAPI()

@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    input_image = Image.open(file.file)
    output_image = remove(input_image)

    img_byte_arr = io.BytesIO()
    output_image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return StreamingResponse(img_byte_arr, media_type="image/png")
