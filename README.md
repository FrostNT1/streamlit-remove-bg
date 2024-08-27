# Streamlit CV App: Background Object Removal

This Streamlit app allows users to upload an image and uses a computer vision AI model to remove people, cars, and artifacts from the background. The project demonstrates the power of computer vision and deep learning in image processing.

## Features

- **Image Upload**: Users can upload an image to the app.
- **AI-Powered Processing**: The app uses a pre-trained AI model to identify and remove objects such as people, cars, and other artifacts from the background.
- **Real-Time Results**: The processed image is displayed directly in the browser.

## Installation

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/FrostNT1/streamlit-remove-bg.git
   cd streamlit-remove-bg
2. Create a new virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate
3. Install the required packages

   ```bash
   pip install -r requirements.txt
4. Run the app

   ```bash
   streamlit run app.py
