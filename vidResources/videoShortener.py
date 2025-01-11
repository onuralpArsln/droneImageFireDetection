import cv2

input_file = "KOZANSON.mp4"
output_file = "KOZANSONShort.mp4"

# Specify start time and duration (in seconds)
start_time = 5  # Start at 30 seconds
duration = 5     # Duration is 5 seconds

# Open the input video
cap = cv2.VideoCapture(input_file)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4

# Output video writer
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Calculate the starting frame and number of frames to process
start_frame = int(start_time * fps)
end_frame = start_frame + int(duration * fps)

# Set the video to the starting frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# Process frames
current_frame = start_frame
while cap.isOpened() and current_frame < end_frame:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    current_frame += 1

# Release resources
cap.release()
out.release()

print(f"5-second clip saved as {output_file}")