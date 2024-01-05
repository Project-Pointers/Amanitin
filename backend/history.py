import json, environments, atexit


class History:
    def __init__(self):
        with open(environments.VARS.HISTORY_DIR, 'r') as f:
            self.history: list = json.load(f)
        atexit.register(self.flush)

    def append(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def dumps(self):
        json.dumps(self.history)

    def flush(self):
        with open(environments.VARS.HISTORY_DIR, 'w+') as f:
            json.dump(self.history, f)


HISTORY = History()
