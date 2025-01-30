from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time

# Generate PDF report from CSV file
def generate_pdf_report(csv_file, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    c.setFont("Helvetica", 12)

    # Add title and timestamp
    c.drawString(100, 750, "System Monitoring Report")
    c.drawString(100, 735, f"Generated on: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Read CSV and add content to PDF
    y = 700
    with open(csv_file, mode='r') as file:
        for line in file:
            if y < 50:  # Move to the next page if content overflows
                c.showPage()
                y = 750
                c.setFont("Helvetica", 12)
            c.drawString(50, y, line.strip())
            y -= 15

    # Save PDF
    c.save()

if __name__ == "__main__":
    generate_pdf_report("5_logs/system_metrics.csv", "3_results/system_report.pdf")