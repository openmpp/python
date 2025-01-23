# ompp_export_excel.py

## Introduction
`ompp_export_excel.py` is a Python utility script to export model output data from an OMPP-compatible SQLite database into Excel files.

By processing the contents of a given SQLite database, `ompp_export_excel.py` creates either a single Excel file with all tables as sheets or multiple Excel files, one for each table, based on the output settings.

## Usage
To run the script, invoke the Python interpreter with `ompp_export_excel.py`, followed by two arguments: the input SQLite database file and the output path where the Excel files will be generated.

### Example Syntax
```bash
python ompp_export_excel.py <input-sqlite-file> <output-path>
```

### Arguments
- `<input-sqlite-file>`: The path to the SQLite database that contains OMPP model output tables.
- `<output-path>`: The path to the directory or file where the script will write the Excel output. If a directory is provided, multiple Excel files are generated (one per table). If a file path is provided, a single Excel file with multiple sheets is created.

## Example
Below is an example of the script run. This example uses the RiskPaths model output database and exports data to the user's desktop folder `excelFiles`.

```bash
C:\OpenM\openm\libopenm\common> python ompp_export_excel.py C:\OpenM\models\RiskPaths\ompp\bin\RiskPaths.sqlite C:\Users\parsaba\Desktop\excelFiles\
```

As the script runs, it displays informational messages for each processed table and confirms where the Excel files are written:

```plaintext
ompp_export_excel: Processing table 'T01_LifeExpectancy'
write_to_excel_file: Data written to 'C:\Users\parsaba\Desktop\excelFiles\T01_LifeExpectancy.xlsx'

ompp_export_excel: Processing table 'T02_TotalPopulationByYear'
write_to_excel_file: Data written to 'C:\Users\parsaba\Desktop\excelFiles\T02_TotalPopulationByYear.xlsx'

ompp_export_excel: Successfully exported 'C:\OpenM\models\RiskPaths\ompp\bin\RiskPaths.sqlite' to 'C:\Users\parsaba\Desktop\excelFiles\'

ompp_export_excel: Database connection closed.
```

This output confirms that each table has been processed and that the corresponding Excel files have been created successfully.

## File Contents
Each generated Excel file contains the full contents of a single table from the SQLite database. If exporting to a single Excel file, each table is written to a separate sheet, with sheet names truncated to 31 characters if necessary.

## Error Handling
If the input database does not exist or the output path is invalid, the script logs an error message and stops. Common errors include:

- **Database file not found**: The specified SQLite database file does not exist.
- **Permission denied**: The script lacks write permissions for the output path.
- **Unexpected runtime errors**: These are logged to help diagnose and fix problems quickly.

## Warnings
When exporting tables with long names, a warning is logged if the sheet name exceeds 31 characters. This limitation is due to Excel's constraints on sheet names.