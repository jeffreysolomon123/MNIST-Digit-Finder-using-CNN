from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps
import io
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = tf.keras.models.load_model("digit_model.h5")

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        data = await image.read()
        img = Image.open(io.BytesIO(data)).convert("L")
        
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        
        img = ImageOps.expand(img, border=20, fill=0)
        img = img.resize((28, 28))
        
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 28, 28, 1)

        prediction = model.predict(img_array)
        digit = int(np.argmax(prediction))
        confidence = float(np.max(prediction))

        return {"digit": digit, "confidence": confidence}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)