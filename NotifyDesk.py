import os
import platform
import time
from typing import Optional


# THE LIBRARY ONLY WORKS WITH LINUX!


def push(title: str = "Title", message: str = "Message",
         delay: Optional[float] = 0, icon: Optional[str] = None) -> bool:  # delay in seconds, icon in .ico format

    try:
        plt = platform.system()

        if plt == "Linux":
            command = f"notify-send '{title}' '{message}'"
            if icon:
                icon_path = os.path.abspath(icon) if os.path.isfile(icon) else icon
                command += f" --icon '{icon_path}'"

        else:
            return False

        if delay > 0:
            time.sleep(delay)

        os.system(command)
        return True

    except Exception as e:
        print(f"Error displaying notification: {str(e)}")
        return False
