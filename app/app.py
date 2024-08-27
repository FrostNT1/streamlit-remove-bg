import streamlit as st
from PIL import Image
from rembg import remove
import io
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_background(image):
    """
    Remove the background from the given image.
    
    Args:
        image (PIL.Image): Input image to process.
    
    Returns:
        PIL.Image: Image with background removed.
    """
    logging.info("Removing background from image...")
    
    # Convert PIL Image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Remove background
    output = remove(img_byte_arr)

    # Convert back to PIL Image
    result = Image.open(io.BytesIO(output))
    
    logging.info("Background removal completed.")
    return result

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("Image Background Remover")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        logging.info(f"Processing uploaded file: {uploaded_file.name}")
        
        # Read the image
        image = Image.open(uploaded_file)
        
        # Display the original image
        st.subheader("Original Image")
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Remove background and display the modified image
        with st.spinner("Removing background..."):
            bg_removed_image = remove_background(image)
        
        st.subheader("Image with Background Removed")
        st.image(bg_removed_image, caption="Background Removed", use_column_width=True)
        
        logging.info("Image processing completed successfully.")

if __name__ == "__main__":
    main()