import csv
from modules.report.exporter import ReportExporter

class CSVExporter(ReportExporter):
    def write_data(self, data, filename):
        with open(filename, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
