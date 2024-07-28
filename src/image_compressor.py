from PIL import Image
import numpy as np
import io

def compress_image(image_path, k):
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Perform SVD
    U, s, Vt = np.linalg.svd(img_array, full_matrices=False)
    
    # Reconstruct the image using only k singular values
    compressed_array = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
    
    # Clip values to be between 0 and 255 and convert to uint8
    compressed_array = np.clip(compressed_array, 0, 255).astype(np.uint8)
    
    # Create a new image from the compressed array
    compressed_img = Image.fromarray(compressed_array)
    
    return compressed_img

def compression_ratio(original, compressed):
    # Save images to bytes objects
    original_bytes = io.BytesIO()
    compressed_bytes = io.BytesIO()
    
    original.save(original_bytes, format='PNG')
    compressed.save(compressed_bytes, format='PNG')
    
    # Get sizes
    original_size = original_bytes.tell()
    compressed_size = compressed_bytes.tell()
    
    return 1 - (compressed_size / original_size)