import os
import sys
import time

import pyautogui


FOLDER = "buttons"
BUTTONS = ["1.png", "2.png", "plus.png", "7.png", "equal.png"]


def open_calculator():
    """Открывает приложение Калькулятор в зависимости от ОС."""
    platform = os.name
    # Windows
    if platform == "nt":
        os.system("start calc")
    # macOS или Linux
    elif platform == "posix":
        os.system("open -a Calculator")
    else:
        raise OSError("Неизвестная операционная система.")


def find_and_click(image, confidence=0.9):
    """Ищет изображение кнопки на экране и кликает по нему."""
    try:
        location = pyautogui.locateOnScreen(image, confidence=confidence)
        pyautogui.click(pyautogui.center(location))
        # Пауза между нажатиями
        time.sleep(0.5)
    except pyautogui.ImageNotFoundException:
        print(f"Кнопка {image} не найдена на экране.")
        sys.exit(1)


def perform_calculation():
    """Автоматизирует выполнение действий на Калькуляторе."""
    for button in BUTTONS:
        find_and_click(f"{FOLDER}/{button}")


if __name__ == "__main__":
    try:
        open_calculator()
        # Ждём, пока приложение загрузится
        time.sleep(2)
        perform_calculation()
    except Exception as e:
        print(f"Произошла ошибка при запуске калькулятора: {e}")
        sys.exit(1)
