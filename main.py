import cv2
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load image
image = cv2.imread("test.jpg")

if image is None:
    print("Image not found!")
    exit()

print("Image loaded successfully!")

# --------------------------------------------------
# 1. Convert image to grayscale
# --------------------------------------------------

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --------------------------------------------------
# 2. Noise reduction using Gaussian Blur
# --------------------------------------------------

blurred_image = cv2.GaussianBlur(
    gray_image,
    (5, 5),
    0
)

# --------------------------------------------------
# 3. Edge Detection using Canny
# --------------------------------------------------

edges = cv2.Canny(
    blurred_image,
    100,
    200
)

# --------------------------------------------------
# 4. Face Detection
# --------------------------------------------------

face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Face detection model not found!")
    exit()

faces = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# --------------------------------------------------
# 5. Basic Image Analysis
# --------------------------------------------------

brightness = gray_image.mean()

print("--------------------------------")
print("SMART IMAGE ANALYSIS RESULTS")
print("--------------------------------")
print("Number of faces detected:", len(faces))
print("Average image brightness:", round(brightness, 2))
print("--------------------------------")

# --------------------------------------------------
# 6. Save processed images
# --------------------------------------------------

cv2.imwrite("output/face_detection.jpg", image)
cv2.imwrite("output/grayscale.jpg", gray_image)
cv2.imwrite("output/blurred.jpg", blurred_image)
cv2.imwrite("output/edges.jpg", edges)

print("Processed images saved in 'output' folder.")

# --------------------------------------------------
# 7. Display results
# --------------------------------------------------

cv2.imshow("Face Detection", image)
cv2.imshow("Grayscale", gray_image)
cv2.imshow("Blurred Image", blurred_image)
cv2.imshow("Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()