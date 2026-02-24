from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
import io

app = FastAPI()

@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    try:
        input_bytes = await file.read()
        output_bytes = remove(input_bytes)

        return StreamingResponse(
            io.BytesIO(output_bytes),
            media_type="image/png"
        )
    except Exception as e:
        return {"error": str(e)}
