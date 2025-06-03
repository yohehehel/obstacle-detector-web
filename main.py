from PIL import Image, ImageDraw
import base64
import io
import random
import os

# Create 10 simple colored square images with PIL
image_data = []
for i in range(10):
    img = Image.new('RGB', (100, 100), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    draw = ImageDraw.Draw(img)
    draw.text((10, 40), f"{i}", fill=(255, 255, 255))

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    base64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')
    image_data.append({
        "filename": f"image_{i}.png",
        "base64": f"data:image/png;base64,{base64_img}",
        "prediction": random.choice(["Obstacle", "No Obstacle"])
    })

# Generate the FastAPI code with embedded images
generated_path = "main.py"
with open(generated_path, "w") as f:
    f.write("from fastapi import FastAPI\n")
    f.write("from fastapi.middleware.cors import CORSMiddleware\n\n")
    f.write("app = FastAPI()\n\n")
    f.write("app.add_middleware(\n")
    f.write("    CORSMiddleware,\n")
    f.write("    allow_origins=[\"*\"],\n")
    f.write("    allow_credentials=True,\n")
    f.write("    allow_methods=[\"*\"],\n")
    f.write("    allow_headers=[\"*\"],\n")
    f.write(")\n\n")
    f.write("import time\n\n")
    f.write("dummy_images = [\n")
    for item in image_data:
        f.write("    {\n")
        f.write(f"        \"filename\": \"{item['filename']}\",\n")
        f.write(f"        \"base64\": \"{item['base64']}\",\n")
        f.write(f"        \"prediction\": \"{item['prediction']}\"\n")
        f.write("    },\n")
    f.write("]\n\n")
    f.write("@app.post(\"/train\")\ndef train_model():\n")
    f.write("    time.sleep(2)\n")
    f.write("    return {\"message\": \"Model training completed (simulated).\"}\n\n")
    f.write("@app.get(\"/predict\")\ndef predict_images():\n")
    f.write("    return {\"results\": dummy_images}\n")

generated_path
