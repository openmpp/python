import os
import sys
import sqlite3
import pandas as pd
from openpyxl import Workbook
from common import logmsg, error, info


def export_to_excel(input_db, output_path):
    try:
        if not os.path.exists(input_db):
            logmsg(error(), "Database Error", f"Input database '{input_db}' not found.")
            return False

        if os.path.isdir(output_path) or output_path.endswith(os.sep):
            # Ensure the directory exists
            if not os.path.exists(output_path):
                os.makedirs(output_path)
                logmsg(info(), "Directory", f"Created output directory '{output_path}'.")
            output_excel = os.path.join(output_path, "exported_data.xlsx")
        else:
            output_excel = output_path
            output_dir = os.path.dirname(output_excel)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
                logmsg(info(), "Directory", f"Created directory for file '{output_dir}'.")

        conn = sqlite3.connect(input_db)
        logmsg(info(), "Database", f"Connected to database '{input_db}'.")

        with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [row[0] for row in cursor.fetchall()]

            if not tables:
                logmsg(info(), "Excel Export", "No tables found in the database.")

            for table_name in tables:
                logmsg(info(), "Database", f"Exporting table '{table_name}' to Excel sheet.")
                table_data = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
                sheet_name = table_name[:31]  # Ensure sheet name length is <= 31
                table_data.to_excel(writer, sheet_name=sheet_name, index=False)

        logmsg(info(), "Excel Export", f"Successfully exported database '{input_db}' to '{output_excel}'.")
        return True

    except Exception as e:
        logmsg(error(), "Excel Export Error", f"Failed to export '{input_db}' to '{output_path}': {str(e)}")
        return False

    finally:
        if 'conn' in locals():
            conn.close()
            logmsg(info(), "Database", "Database connection closed.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ompp_export_excel.py <input-sqlite> <output-path>")
        sys.exit(1)

    input_db = sys.argv[1]
    output_path = sys.argv[2]

    export_to_excel(input_db, output_path)