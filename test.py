import time
import threading
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.completion import WordCompleter

from internal.cache import Cache
from internal.enums import Burnrates, Resource_types
from internal.enums.task_types import commands
import os

cache = Cache()
resource_lock = threading.Lock()
stop_event = threading.Event()

# Set up autocompletion from your command dictionary keys
cli_completer = WordCompleter(list(commands.keys()), ignore_case=True)

def mindeple():
    while not stop_event.is_set():
        cache.buildings.buildingresourcecosts()
        cache.resources.resourcedeplete(resource_lock)
        time.sleep(1)

def display_loop():
    num_lines = len(Resource_types) + 3  # header + footer + resource lines

    while not stop_event.is_set():
        # Move up and clear previous output
        for _ in range(num_lines):
            print("\x1b[1A\x1b[2K", end='')  # \x1b[1A = move up, \x1b[2K = clear line

        values = cache.resources.getresources()
        print("=============== Resource Overview ===============")
        for type in Resource_types:
            name = type.name.lower()
            burnrate = getattr(Burnrates, name)
            print(f"{name.title():<12}: {values[name]:<5} : Burnrate: {burnrate}")
        print("=" * 50)

        time.sleep(1)



def input_loop():
    session = PromptSession(completer=cli_completer)
    with patch_stdout():  # allows background prints without corrupting input
        while not stop_event.is_set():
            try:
                option = session.prompt("Enter a command: ")
                if option.strip().lower() in ("exit", "quit"):
                    stop_event.set()
                    break

                # Run associated command
                commands[option].run("hello")

            except (KeyError, ValueError):
                print("Invalid command.")
            except (EOFError, KeyboardInterrupt):
                stop_event.set()
                break

def main():
    threads = [
        threading.Thread(target=mindeple, daemon=True),
        threading.Thread(target=display_loop, daemon=True),
        threading.Thread(target=input_loop)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
