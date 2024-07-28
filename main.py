import numpy as np
from src.visualizer import visualize_subspaces
from src.image_compressor import compress_image, compression_ratio
from PIL import Image

def main():
    # Example matrix
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    print("Original Matrix:")
    print(matrix)
    print("\nVisualizing subspaces...")
    visualize_subspaces(matrix)

    # Image compression
    image_path = 'data/kiyo.jpg'
    original_img = Image.open(image_path).convert('L')  # Convert to grayscale
    
    print("\nCompressing image...")
    
    # Try different compression levels
    for k in [10, 50, 100]:
        compressed_img = compress_image(image_path, k)
        
        ratio = compression_ratio(original_img, compressed_img)
        print(f"Compression ratio (k={k}): {ratio:.2%}")

        compressed_img.show(title=f"Compressed Image (k={k})")

    original_img.show(title="Original Image")

if __name__ == "__main__":
    main()