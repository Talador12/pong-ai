import time
import cv2
from mss.windows import MSS as mss
import numpy as np

# TESTED PIL at ~15 fps


def screen_record(
    left_right_mode=True,
    game_monitor=1,
    pos_set={"top": 100, "left": 1025, "width": 800, "height": 640},
):
    sct = mss()
    monitor = sct.monitors[game_monitor]
    monitor["mon"] = game_monitor

    if left_right_mode:
        # Left/Right Mode
        return np.asarray(sct.grab(pos_set))
    # Top/Bottom Mode
    return np.rot90(np.asarray(sct.grab(monitor)))


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
