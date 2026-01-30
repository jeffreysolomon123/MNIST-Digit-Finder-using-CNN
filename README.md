### A simple handwritten digit recognition application using a Convolutional Neural Network (CNN) trained on the MNIST dataset. You can draw digits (0–9) on a browser canvas, and the model predicts the digit in real time via a FastAPI backend.
![Untitled video - Made with Clipchamp (1)](https://github.com/user-attachments/assets/52af191b-8000-45c7-bfff-3881a7fa8670)
**Model Architecture**
- Input shape: 28 × 28 × 1 (grayscale image)
- Convolutional layers:
- Conv2D with 32 filters (3×3)
- Conv2D with 64 filters (3×3)
- Pooling layers: 2 × MaxPooling (2×2)
- Fully connected layer: 128 neurons (ReLU)
- Output layer: 10 neurons (Softmax)

**Training Configuration**
Dataset size:
- Training samples: 60,000
- Test samples: 10,000
- Optimizer: Adam
- Loss function: Sparse Categorical Cross-Entropy
- Batch size: 64
- Epochs: 5
- Validation split: 10%

**Model Performance**
- Training accuracy: ~99%
- Test accuracy: ~99.0–99.1%
- Test loss: ~0.03
- Inference time: ~8 ms per batch (CPU)

**Full-Stack Implementation**
- Frontend uses an HTML5 Canvas (280×280 px) to capture handwritten digit input.
- Drawn images are converted to binary blobs and sent to the backend via HTTP POST requests.
- Backend is implemented using FastAPI, exposing a /predict endpoint for model inference.
- Image preprocessing and prediction are performed server-side using TensorFlow.
- The backend returns the predicted digit (0–9) as a JSON response.

