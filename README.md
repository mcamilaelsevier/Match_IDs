
## Excel Sheet Matching Tool

This script matches UUIDs with ScopusIDs based on a common ID within the same Excel file. The Excel file should contain two sheets: one with UUIDs and the other with ScopusIDs, both linked by a common ID.

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `tkinter`
  - `openpyxl`

Install the required libraries using pip:

```sh
pip install pandas openpyxl
```

### Excel File Structure

The Excel file should contain two sheets:

- **Sheet1**: Contains the columns `ID` and `UUID`
- **Sheet2**: Contains the columns `ID` and `ScopusID`

### Script Usage

1. **Run the script:**

```sh
python match_ids.py
```

2. **Use the graphical interface to select the Excel file.**

A window will open to upload the Excel file:

![image](https://github.com/user-attachments/assets/262b816b-dfa5-4826-8cbf-13231ae0efaf)


4. **The matched results will be saved to a new Excel file named `matched_results.xlsx`.**


### Notes

- The script uses the `pandas` library to read and merge data from the Excel file.
- The script uses `tkinter` to create a graphical user interface for selecting the Excel file and displaying messages.
- The matched results are saved to a new Excel file named `matched_results.xlsx` in the same directory as the script.

Make sure to replace any placeholder values in the script with your actual file paths and other relevant information. Also, replace `path_to_image` with the actual path to the image file showing the window to upload the Excel file.
