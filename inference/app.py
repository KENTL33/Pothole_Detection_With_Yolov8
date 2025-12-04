import gradio as gr
from ultralytics import YOLO
import PIL.Image as Image

# 1. Load your trained model
model = YOLO("best.pt")

# 2. Define the function to make predictions
def predict_image(img):
    # Run the model on the input image
    results = model.predict(img)
    
    # Plot the results (draw boxes)
    # This returns a numpy array in BGR format
    result_plot = results[0].plot()
    
    # Convert the array (BGR) back to an image (RGB) for display
    # (YOLO plots are BGR by default, but web browsers like RGB)
    result_image = Image.fromarray(result_plot[..., ::-1]) 
    
    return result_image

# 3. Create the Web Interface
iface = gr.Interface(
    fn=predict_image,                  # The function to run
    inputs=gr.Image(type="pil"),       # Input: User uploads an image
    outputs=gr.Image(type="pil"),      # Output: The image with boxes
    title="Pothole Detection AI",      # Title of your app
    description="Upload a road image to detect potholes using YOLOv8."
)

# 4. Launch the app
iface.launch()
