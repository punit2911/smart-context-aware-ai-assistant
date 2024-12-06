from fastapi import APIRouter, File, UploadFile
from PIL import Image
import io
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

router = APIRouter()

# Endpoint to upload an image and receive a caption
@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_data = await file.read()
        # Open the image
        image = Image.open(io.BytesIO(image_data))

        # Prepare the image for processing
        inputs = processor(images=image, return_tensors="pt")
        # Generate a caption
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        return {"caption": caption}
    except Exception as e:
        return {"error": f"Failed to process the image: {str(e)}"}
