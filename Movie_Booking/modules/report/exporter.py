from modules.report.logger import Logger

class ReportExporter:
    def export(self, data, filename):
        try:
            self._prepare(filename)
            self.write_data(data, filename)
            self._finish(filename)
        except Exception as e:
            Logger.log(f"Export failed: {str(e)}")

    def _prepare(self, filename):
        print(f"Preparing export to {filename}...")

    def _finish(self, filename):
        print(f"Export done: {filename}")

    def write_data(self, data, filename):
        raise NotImplementedError("write_data() must be implemented in subclass")
