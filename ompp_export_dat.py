import sys
import os
import sqlite3
from common import logmsg, error, info, run_sqlite_script, write_to_dat_file

def print_usage():
    """Print usage instructions."""
    print(f"Usage: {sys.argv[0]} <input-sqlite-file> <output-directory>")
    print("Options:")
    print("  -h, --help    print usage message and exit")
    print("  -v, --version print version and exit")

def export_to_dat(input_db, output_dir):
    try:
        if not os.path.exists(input_db):
            logmsg(error(), "ompp_export_dat", f"Input SQLite database '{input_db}' not found.")
            return 1

        if not os.path.exists(output_dir):
            logmsg(error(), "ompp_export_dat", f"Output directory '{output_dir}' does not exist.")
            return 1

        conn = sqlite3.connect(input_db)
        cursor = conn.cursor()

        cursor.execute("SELECT table_name FROM table_dic ORDER BY table_name;")
        tables = [row[0] for row in cursor.fetchall()]

        for table in tables:
            logmsg(info(), "ompp_export_dat", f"Processing table '{table}'")
            cursor.execute(f"SELECT * FROM {table};")
            data = cursor.fetchall()
            columns = [description[0] for description in cursor.description]

            dat_file = os.path.join(output_dir, f"{table}.dat")

            write_to_dat_file(table, columns, data, dat_file)

        logmsg(info(), "ompp_export_dat", f"Successfully exported '{input_db}' to '{output_dir}'")
        return 0

    except sqlite3.Error as e:
        logmsg(error(), "ompp_export_dat", f"Database error: {e}")
        return 1

    except Exception as e:
        logmsg(error(), "ompp_export_dat", f"Unexpected error: {e}")
        return 1

    finally:
        if 'conn' in locals():
            conn.close()
            logmsg(info(), "ompp_export_dat", "Database connection closed.")

def main(argv):
    script_name = 'ompp_export_dat'
    script_version = '1.0'

    if '-h' in argv or '--help' in argv:
        print_usage()
        sys.exit(0)
    if '-v' in argv or '--version' in argv:
        print(f"{script_name} version {script_version}")
        sys.exit(0)

    if len(argv) != 2:
        print_usage()
        sys.exit(2)

    input_db = argv[0]
    output_dir = argv[1]

    sys.exit(export_to_dat(input_db, output_dir))

if __name__ == "__main__":
    main(sys.argv[1:])