from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageDraw
import base64
import io
import time
import random

app = FastAPI()

# Enable CORS for frontend (Elementor)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Generate 10 base64 images with labels
def generate_dummy_images():
    images = []
    for i in range(10):
        img = Image.new('RGB', (100, 100), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        draw = ImageDraw.Draw(img)
        draw.text((30, 40), f"{i}", fill=(255, 255, 255))

        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        base64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')
        images.append({
            "filename": f"image_{i}.png",
            "base64": f"data:image/png;base64,{base64_img}",
            "prediction": random.choice(["Obstacle", "No Obstacle"])
        })
    return images

# Store dummy predictions once (can be refreshed per call if needed)
dummy_images = generate_dummy_images()

@app.post("/train")
def train_model():
    time.sleep(2)  # Simulated training
    return {"message": "Model training completed (simulated)."}

@app.get("/predict")
def predict_images():
    return {"results": dummy_images}

@app.get("/")
def root():
    return {"message": "FastAPI backend is running. Use /train or /predict."}
