# import pyautogui
# import time
# # 1098,1035 39,43,68 #272B44
# # pyautogui.mouseInfo()
# # 1386,1038 123,131,235 #7B83EB

# start_time = time.perf_counter_ns()
# pyautogui.hotkey('winleft', 'r')
# time.sleep(1)
# pyautogui.write('Desktop')
# pyautogui.press('enter')

# end_time = time.perf_counter_ns()


# elapsed_time = (end_time - start_time) / 1_000_000  # Convert from nanoseconds to milliseconds

# print(f"Elapsed time: {elapsed_time} milliseconds")

import pyautogui
import time

# Start timer
start_time = time.time()

# # Launch Notepad
# pyautogui.hotkey('winleft', 'r')
# time.sleep(1)
# pyautogui.write('Desktop')
# pyautogui.press('enter')
# time.sleep(1)

# # Wait for Notepad window to appear
# # notepad_window = None
# # while not notepad_window:
# #     notepad_window = pyautogui.locateOnScreen('notepad_window.png')
# #     time.sleep(1)

# # Wait for Notepad window to disappear
# # while notepad_window:
# #     notepad_window = pyautogui.locateOnScreen('notepad_window.png')
# #     time.sleep(1)

# # Stop timer
# end_time = time.time()

# # Calculate load time
# load_time = end_time - start_time
# print(f"Load time: {load_time:.2f} seconds")

import time
import pyautogui

# Launch the app
start_time = time.perf_counter()
pyautogui.hotkey('winleft', 'r')
time.sleep(1)
pyautogui.write('Desktop')
pyautogui.press('enter') # example click to launch the app
end_time = time.perf_counter()

load_time_ms = (end_time - start_time) * 1000
print("Load time:", load_time_ms, "ms")