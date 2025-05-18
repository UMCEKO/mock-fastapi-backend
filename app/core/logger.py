import traceback

import colorama


class Logger:
    def __init__(self, log_dir = "log.txt", level = "info"):
        self.log_file = open(log_dir, "w")
        if level not in ["info", "error", "warn"]:
            raise Exception("Invalid level passed to logger. Valid values: info, error, warn")
        self.level: str = level

    @staticmethod
    def get_stack():
        return [trace.strip() for trace in traceback.format_stack()
            if "logger.py" not in trace]

    def error(self, message: str):
        stack = "\n".join(self.get_stack())
        self.write_log(f"Error: {colorama.Fore.LIGHTRED_EX}{stack}{colorama.Fore.RESET}\n"
                       f"Message: {colorama.Fore.RED}{message}")

    def info(self, message: str):
        if self.level in ["info"]:
            frame = self.get_stack().pop()
            self.write_log(f"Info from: {colorama.Fore.LIGHTBLUE_EX}{frame}{colorama.Fore.RESET}\n"
                           f"Message: {colorama.Fore.BLUE}{message}")

    def warn(self, message: str):
        if self.level in ["info", "warn"]:
            frame = self.get_stack().pop()
            self.write_log(f"Warning from: {colorama.Fore.LIGHTYELLOW_EX}{frame}{colorama.Fore.RESET}\n"
                           f"Message: {colorama.Fore.YELLOW}{message}")

    def write_log(self, text: str):
        print(text)
        self.log_file.write(text + "\n\n")

logger = Logger()