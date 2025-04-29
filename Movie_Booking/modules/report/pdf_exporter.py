from modules.report.exporter import ReportExporter

class PDFExporter(ReportExporter):
    def write_data(self, data, filename):
        with open(filename, 'w') as f:
            f.write("PDF EXPORT SIMULASI\n\n")
            for row in data:
                f.write("\n".join(f"{k}: {v}" for k, v in row.items()))
                f.write("\n---\n")
