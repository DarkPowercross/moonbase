import readline
from internal.tasks import Build, View
from dataclasses import dataclass
from enum import Enum
from typing import Callable, Any


@dataclass
class Task:
    name: str
    description: str
    callback: Callable[..., Any]

    def run(self, *args, **kwargs) -> Any:
        return self.callback(*args, **kwargs)


class Task_types(Enum):
    BUILD = Build
    VIEW = View


    def to_task(self) -> Task:
        instance = self.value()
        return Task(
            name=instance.name,
            description=instance.description,
            callback=instance.run
        )


commands = {
    "build": Task_types.BUILD.to_task(),
    "view": Task_types.VIEW.to_task()
}


def completer(text, state):
    matches = [cmd for cmd in commands if cmd.startswith(text)]
    return matches[state] if state < len(matches) else None

