open_vscode()
# open extension icon
pyautogui.hotkey('ctrl', 'shift', 'x')
time.sleep(2)

# Install clangd
install_extension('clangd')