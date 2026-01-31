class ProgressHandler:
    def __init__(self):
        self.done = False

    def update(self, bytes_sent, total_bytes):
        if self.done:
            return

        percent = (bytes_sent / total_bytes * 100) if total_bytes > 0 else 0
        mb_sent = bytes_sent / (1024 * 1024)
        mb_total = total_bytes / (1024 * 1024)

        bar_width = 30
        filled = int(bar_width * percent / 100)
        bar = "#" * filled + "-" * (bar_width - filled)

        print(
            f"\r[{bar}] {percent:6.2f}% {mb_sent:7.1f}/{mb_total:.1f} MiB",
            end="",
            flush=True,
        )

        if bytes_sent >= total_bytes:
            print()
            self.done = True
