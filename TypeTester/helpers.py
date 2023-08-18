import keyboard

from constants import KEY_BACKSAPCE, KEY_SHIFT, KEY_ENTER


def display_value(heading, value):
    """
    Display a formatted heading and value.

    Args:
        heading (str): The heading or label for the value.
        value (str or float): The value to be displayed.

    Returns:
        None
    """
    print(
        f"{heading}: {value:.2f}" if isinstance(value, float) else f"{heading}: {value}"
    )


def record_to_word(record):
    """
    Convert a list of recorded keystrokes into a list of characters.

    Args:
        record (list): A list of recorded keystrokes.

    Returns:
        list: A list of characters extracted from the recorded keystrokes.
    """
    typed_word = []
    shift_active = False
    for char in record:
        if char != KEY_BACKSAPCE and char != KEY_SHIFT and char != KEY_ENTER:
            if shift_active:
                char = char.upper()
                shift_active = False
            typed_word.append(char)
        elif char == KEY_BACKSAPCE:
            typed_word.pop()
        elif char == KEY_SHIFT:
            shift_active = not shift_active
    return typed_word


def record_keystrokes():
    """
    Record keystrokes until the 'Enter' key is pressed.

    Returns:
        list: A list of recorded keystrokes.
    """
    key_record = []
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key_record.append(event.name)
        elif event.event_type == keyboard.KEY_UP:
            if event.name == "enter":
                break
    return key_record
