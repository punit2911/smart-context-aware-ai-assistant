from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
from io import BytesIO

# Load the CLIP model and processor
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")

def analyze_image(image_data: bytes) -> dict:
    """
    Analyze an image and classify it based on text descriptions.
    Returns the predicted class and probability.
    """
    # Convert byte data to image
    image = Image.open(BytesIO(image_data))
    
    # Define text prompts for image classification
    text_prompts = ["a photo of a dog", "a photo of a cat", "a photo of a man", "a photo of a woman"]
    
    # Preprocess image and text for CLIP
    inputs = processor(text=text_prompts, images=image, return_tensors="pt", padding=True)
    
    # Perform inference with CLIP
    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # similarity score between image and text
    probs = logits_per_image.softmax(dim=1)  # Convert logits to probabilities
    
    # Return the class with the highest probability
    predicted_class = text_prompts[torch.argmax(probs)]
    probability = float(torch.max(probs).item())
    
    return {"predicted_class": predicted_class, "probability": probability}

