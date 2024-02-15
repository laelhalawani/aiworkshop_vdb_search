# Import the clip module from the CLIP library and the device management from PyTorch
import clip
import torch
from PIL import Image

# Load the CLIP model and its preprocessing pipeline. "ViT-B/32" specifies the model architecture and version. 
# 'device' specifies the hardware (CPU/GPU) on which the model will run.
device = 'cpu'
model, preprocess = clip.load("ViT-B/32", device=device)

# Define a class method to encode images.
def encode_image(image):
    # Preprocess the image (resize, crop, normalize) and add a batch dimension so it can be processed by the model.
    image = preprocess(image).unsqueeze(0).to(device)
    # Disable gradient calculations to save memory and computations since we're only doing inference.
    with torch.no_grad():
        # Encode the preprocessed image to get the image features (embeddings).
        image_features = model.encode_image(image)
        # Extract the first (and only) item from the features to get the embedding vector.
        # Normally batches of images are used, that's why we need to extract the first item.
        image_embeddings = image_features[0]
        # Convert the tensor of embeddings to a Python list for easier handling.
        image_embeddings: list = list(image_embeddings.numpy().astype(float))
        # Print a success message with the type of the image_embeddings variable.
        print(f"Created embeddings for image, type {type(image_embeddings)}")
    # Return the list of image embeddings.
    return image_embeddings

# Define a function to encode an image given its file path.
def encode_image_from_path(path):
    # Open the image file from the given path.
    image = Image.open(path) if isinstance(path, str) else path
    # Use the encode_image method to encode this image and return the embeddings.
    return encode_image(image)

def encode_string(text):
    # Example text
    tokens = clip.tokenize(text).to(device)
    # Encode text
    with torch.no_grad():
        text_features = model.encode_text(tokens)
        text_embeddings = text_features[0]
        print(f"Successfully encoded and converted {type(text_embeddings)}")
        text_embeddings: list = list(text_embeddings.numpy().astype(float))
    return text_embeddings

