import time
import cv2
from mss.windows import MSS as mss
import numpy as np
import math

# TESTED PIL at ~15 fps


def screen_record(game_monitor=1):
    sct = mss()
    monitor = sct.monitors[game_monitor]
    monitor["mon"] = game_monitor

    # Infer the pos_set from the monitor size, use the whole monitor as the image
    pos_set = monitor

    # Idleon specific image sizing, based on monitor size
    pos_set["top"] = math.floor(pos_set["top"] + pos_set["height"] * 0.085)
    pos_set["left"] = math.floor(pos_set["left"] + pos_set["width"] * 0.06)
    pos_set["width"] = math.floor(pos_set["width"] * 0.685)
    pos_set["height"] = math.floor(pos_set["height"] * 0.71)

    return np.asarray(sct.grab(pos_set)), pos_set


if __name__ == "__main__":
    start_time = time.time()
    x = 1  # displays the frame rate every 1 second
    counter = 0

    try:
        while True:
            img = screen_record()

            counter += 1
            if (time.time() - start_time) > x:
                print("FPS: ", counter // (time.time() - start_time))
                counter = 0
                start_time = time.time()

            cv2.imshow("window", img)
            if cv2.waitKey(10) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

    except KeyboardInterrupt:
        pass
