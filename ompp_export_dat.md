# ompp_export_dat.py

## Introduction
`ompp_export_dat.py` is a Python utility script to export model output data from an OMPP-compatible SQLite database into `.dat` files.

By processing the contents of a given SQLite database, `ompp_export_dat.py` creates a series of `.dat` files, one for each table found in the database.

## Usage
To run the script, invoke the Python interpreter with `ompp_export_dat.py`, followed by two arguments: the input SQLite database file and the output directory where the `.dat` files will be generated.

### Example Syntax
```bash
python ompp_export_dat.py <input-sqlite-file> <output-directory>
```

### Arguments
- `<input-sqlite-file>`: The path to the SQLite database that contains OMPP model output tables.
- `<output-directory>`: The path to the directory where the script will write the generated `.dat` files.

## Example
Below is an example invocation of the script on a Windows system. This example uses the RiskPaths model output database and exports data to the user's desktop folder `ompp_exportDAT`.

```bash
C:\OpenM\openm\libopenm\common> python ompp_export_dat.py C:\OpenM\models\RiskPaths\ompp\bin\RiskPaths.sqlite C:\Users\parsaba\Desktop\ompp_exportDAT
```

As the script runs, it displays informational messages for each processed table and confirms where the `.dat` file is written:

```plaintext
ompp_export_dat: Processing table 'T01_LifeExpectancy'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T01_LifeExpectancy.dat'

ompp_export_dat: Processing table 'T02_TotalPopulationByYear'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T02_TotalPopulationByYear.dat'

ompp_export_dat: Processing table 'T03_FertilityByAge'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T03_FertilityByAge.dat'

ompp_export_dat: Processing table 'T04_FertilityRatesByAgeGroup'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T04_FertilityRatesByAgeGroup.dat'

ompp_export_dat: Processing table 'T05_CohortFertility'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T05_CohortFertility.dat'

ompp_export_dat: Processing table 'T06_BirthsByUnion'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T06_BirthsByUnion.dat'

ompp_export_dat: Processing table 'T07_FirstUnionFormation'
write_to_dat_file: Data written to 'C:\Users\parsaba\Desktop\ompp_exportDAT\T07_FirstUnionFormation.dat'

ompp_export_dat: Successfully exported 'C:\OpenM\models\RiskPaths\ompp\bin\RiskPaths.sqlite' to 'C:\Users\parsaba\Desktop\ompp_exportDAT'

ompp_export_dat: Database connection closed.
```

This output confirms that each table has been processed and that the corresponding `.dat` files have been created successfully.

## File Contents
Within each generated `.dat` file, the script includes a header line with the table name and columns, followed by rows of data. These rows are space-separated by default.

## Error Handling
If the input database does not exist or the output directory is invalid, the script logs an error message and stops. Database connectivity issues or unexpected runtime errors are also reported to help you diagnose and fix problems quickly.