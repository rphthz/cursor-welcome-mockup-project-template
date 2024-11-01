import sys
import time

def animate_text(text: str, delay: float = 0.1) -> None:
    """
    Animate text character by character.
    
    Args:
        text (str): Text to animate
        delay (float): Delay between characters in seconds
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def loading_animation(iterations: int = 20, delay: float = 0.1) -> None:
    """
    Display a loading animation.
    
    Args:
        iterations (int): Number of animation cycles
        delay (float): Delay between frames in seconds
    """
    animation = "|/-\\"
    for i in range(iterations):
        sys.stdout.write("\r" + "Loading " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(delay)
    print("\nDone!")
