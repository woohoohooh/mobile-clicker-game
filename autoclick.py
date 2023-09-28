import pyautogui
import time
import random

target_x = 460
target_y = 1030
target_x_a = 900
target_y_a = 140

target_x2 = 520
target_y2 = 1030
target_x2_a = 900
target_y2_a = 150

target_x3 = 600
target_y3 = 1030
target_x3_a = 890
target_y3_a = 155

target_x4 = 680
target_y4 = 1030
target_x4_a = 900
target_y4_a = 140

target_x5 = 730
target_y5 = 1030
target_x5_a = 895
target_y5_a = 155

target_x6 = 730
target_y6 = 1030
target_x6_a = 895
target_y6_a = 150

# --------------------

interval = random.randint(1,5)

try:
    while True:

        random_x = random.randint(-10, 10)
        random_y = random.randint(-10, 10)

        final_x = target_x + random_x
        final_y = target_y + random_y

        random_x_a = random.randint(-10, 10)
        random_y_a = random.randint(-10, 10)

        final_x_a = target_x_a + random_x_a
        final_y_a = target_y_a + random_y_a

        random_x2 = random.randint(-10, 10)
        random_y2 = random.randint(-10, 10)

        final_x2 = target_x2 + random_x2
        final_y2 = target_y2 + random_y2

        random_x2_a = random.randint(-10, 10)
        random_y2_a = random.randint(-10, 10)

        final_x2_a = target_x2_a + random_x2_a
        final_y2_a = target_y2_a + random_y2_a

        random_x3 = random.randint(-10, 10)
        random_y3 = random.randint(-10, 10)

        final_x3 = target_x3 + random_x3
        final_y3 = target_y3 + random_y3

        random_x3_a = random.randint(-10, 10)
        random_y3_a = random.randint(-10, 10)

        final_x3_a = target_x3_a + random_x3_a
        final_y3_a = target_y3_a + random_y3_a

        random_x4 = random.randint(-10, 10)
        random_y4 = random.randint(-10, 10)

        final_x4 = target_x4 + random_x4
        final_y4 = target_y4 + random_y4

        random_x4_a = random.randint(-10, 10)
        random_y4_a = random.randint(-10, 10)

        final_x4_a = target_x4_a + random_x4_a
        final_y4_a = target_y4_a + random_y4_a

        random_x5 = random.randint(-10, 10)
        random_y5 = random.randint(-10, 10)

        final_x5 = target_x5 + random_x5
        final_y5 = target_y5 + random_y5

        random_x5_a = random.randint(-10, 10)
        random_y5_a = random.randint(-10, 10)

        final_x5_a = target_x5_a + random_x5_a
        final_y5_a = target_y5_a + random_y5_a

        random_x6 = random.randint(-10, 10)
        random_y6 = random.randint(-10, 10)

        final_x6 = target_x5 + random_x6
        final_y6 = target_y5 + random_y6

        random_x6_a = random.randint(-10, 10)
        random_y6_a = random.randint(-10, 10)

        final_x6_a = target_x6_a + random_x6_a
        final_y6_a = target_y6_a + random_y6_a

        pyautogui.moveTo(final_x, final_y, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x_a, final_y_a, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x2, final_y2, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x2_a, final_y2_a, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x3, final_y3, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x3_a, final_y3_a, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x4, final_y4, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x4_a, final_y4_a, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x5, final_y5, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x5_a, final_y5_a, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

        pyautogui.moveTo(final_x6_a, final_y6_a, duration=0.5)
        pyautogui.click()

        time.sleep(interval)

except KeyboardInterrupt:
    print("Stop.")
