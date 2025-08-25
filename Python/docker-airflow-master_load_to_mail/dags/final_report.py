import logging
from airflow.models import Variable

def generate_final_status(**context):
    status_log = Variable.get("pipeline_status_log", default_var="[]", deserialize_json=True)

    logging.info(f"Loaded status_log: {status_log}")

    report_lines = ["Pipeline Execution Report:\n"]
    for log in status_log:
        if isinstance(log, dict) and {'task_id', 'status', 'timestamp'} <= log.keys():
            line = f"{log['task_id']} => {log['status']} at {log['timestamp']}"
        else:
            line = f"⚠️ Unexpected log entry: {log}"
        report_lines.append(line)

    report = "\n".join(report_lines)

    report_path = "/usr/local/airflow/op_files/pipeline_status_report.txt"
    with open(report_path, "w") as f:
        f.write(report)

    logging.info(f"✅ Pipeline report written to {report_path}")
    return report_path
