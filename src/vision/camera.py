"""
camera.py - Opens a video source (phone stream or webcam) and displays frames.
"""
import cv2


def open_camera(source):
    """
    Open a video source.
    source: a URL string (e.g. "http://192.168.1.5:8080/video") for the phone,
            or an int (0) for the laptop webcam.
    Returns an opened cv2.VideoCapture object.
    """
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video source: {source}")
    return cap


if __name__ == "__main__":
    # Change this to the address shown in the IP Webcam app (+ "/video")
    SOURCE = 0

    cap = open_camera(SOURCE)
    printed_shape = False

    while True:
        ok, frame = cap.read()          # ok = True if a frame was grabbed
        if not ok:
            print("Stream ended or frame could not be read.")
            break

        if not printed_shape:
            print("Frame shape:", frame.shape)   # (height, width, channels)
            printed_shape = True

        cv2.imshow("ChessVision", frame)

        # Wait 1 ms for a key; quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()