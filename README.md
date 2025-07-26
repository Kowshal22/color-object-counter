## Color-Based Object Counter

A computer vision project that detects and counts objects of a specific color in **real-time webcam feeds** and **static images** using OpenCV. Designed for foundational CV learners and developers looking to explore HSV color filtering and contour-based detection.

## Features

- ✅ Real-time webcam object detection
- 🖼️ Image-based object detection with bounding boxes
- 🎨 HSV color space filtering for precise color segmentation
- 📏 Dynamic contour area filtering to avoid noise
- 📸 Object count display over live feed

## 📁 Project Structure
- webcam_counter.py
- image_counter.py          
- func.py                   
- requirements.txt          
- README.md                
- .gitignore 

## How to Run
git clone https://github.com/yourusername/color-object-counter.git
cd color-object-counter
pip install -r requirements.txt
python webcam_counter.py
python image_counter.py

## Customization
- Edit func.py → get_color() to modify the target BGR color and adjust the HSV range accordingly. You can also fine-tune the contour filtering  threshold in image_counter.py and webcam_counter.py for better accuracy.

## Learning Outcomes 
- Color space transformation (BGR → HSV)
- Binary mask creation for color filtering
- Image thresholding and morphological operations
- Bounding box drawing and contour analysis
- Real-time frame processing with OpenCV



