import pyautogui
import time


def open_vscode():
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Visual Studio Code')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(pyautogui.locateOnScreen('Script_image/max.png'))
    time.sleep(4)
    # open extension icon
    pyautogui.hotkey('ctrl', 'shift', 'x')
    time.sleep(2)





def install_extension(extension_name):

    pyautogui.typewrite(extension_name)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for extension installation
    
    

    # Find and click the "Install" button
    install_button_location = pyautogui.locateOnScreen('Script_image/install.png',confidence=0.7)

    if install_button_location is not None:

        install_button_center = pyautogui.center(install_button_location)
        pyautogui.click(install_button_center)
        time.sleep(3)  # Wait for installation to complete

    else:

        print(f"Failed to find the 'Install' button for extension: {extension_name}")

   

 # look for search box again and delete its content
    button_location = pyautogui.locateOnScreen('Script_image/searchbox.png',confidence=0.6)

    if button_location is not None:

        button_center = pyautogui.center(button_location)

        pyautogui.click(button_center[0],button_center[1]+45)

        time.sleep(2)  # Wait for installation to complete

        for i in range(len(extension_name)):
            pyautogui.press('backspace')

    else:

        print(f"Failed to find the the search bar")





open_vscode()


# Install clangd
install_extension('clangd')

# Install C++ TestMate
install_extension('C++ TestMate')

# Install C++ Helper
install_extension('C++ Helper')

# Install CMake
install_extension('CMake')

# Install CMake Tools
install_extension('CMake Tools')


