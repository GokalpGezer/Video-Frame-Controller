import cv2
import time


def play_video_with_frame_capture(video_path, frame_rate):
    # Check if the frame rate is valid
    if frame_rate < 1 or frame_rate > 24:
        raise ValueError("Frame rate must be between 1 and 24 frames per second.")

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Get the frame width and height for writing the output video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to write the frames into a new video file
    output_filename = 'output20sec_video.avi'
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec
    out = cv2.VideoWriter(output_filename, fourcc, frame_rate, (frame_width, frame_height))

    # Calculate the delay based on the frame rate (in milliseconds)
    delay = int(1000 / frame_rate)

    # Start time for the 20 seconds playback
    start_time = time.time()
    total_frames = frame_rate * 20  # Total frames to capture for 20 seconds
    frame_count = 0  # Frame counter

    # Scale factor to enlarge the video
    scale_factor = 2

    while cap.isOpened() and frame_count < total_frames:
        ret, frame = cap.read()

        if not ret:
            print("End of video or failed to read frame.")
            break

        # Resize the frame to make it larger (double size)
        enlarged_frame = cv2.resize(frame, (frame_width * scale_factor, frame_height * scale_factor))

        # Display the enlarged frame
        cv2.imshow('Video Playback', enlarged_frame)

        # Write the original-sized frame to the output video file
        out.write(frame)

        frame_count += 1  # Increment the frame counter

        # Check if 20 seconds have passed
        elapsed_time = time.time() - start_time
        if elapsed_time >= 20:
            print("Playback ended after 20 seconds.")
            break

        # Wait for the specified delay and check if 'q' is pressed to quit
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            print("Playback interrupted by user.")
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# Example usage with your specific video path
video_path = r'C:\Users\Gokalp\Desktop\video.mp4'  # Use raw string for Windows paths

# Ask user for the frame rate
frame_rate = int(input("Please enter the frame rate (1-24 fps): "))

# Call the function
play_video_with_frame_capture(video_path, frame_rate)
