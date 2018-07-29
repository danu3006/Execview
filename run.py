from report import Report

report = Report(csv_file_path='docs/chicago-bulls.csv')
print(report.to_json())
