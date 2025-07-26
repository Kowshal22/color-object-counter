def get_color(color):
    import numpy as np
    import cv2

    # Convert BGR to HSV
    bgr_color = np.uint8([[color]])
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)[0][0]
    hue = hsv_color[0]

    # Define lower and upper HSV bounds
    if hue >= 165:
        lower = np.array([hue - 10, 100, 100])
        upper = np.array([180, 255, 255])
    elif hue <= 15:
        lower = np.array([0, 100, 100])
        upper = np.array([hue + 10, 255, 255])
    else:
        lower = np.array([hue - 10, 100, 100])
        upper = np.array([hue + 10, 255, 255])

    return lower, upper

