class Logger:
    @staticmethod
    def log(message):
        with open("log.txt", "a") as f:
            f.write("[ERROR] " + message + "\n")
