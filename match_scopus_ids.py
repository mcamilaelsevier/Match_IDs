import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to match UUID with ScopusID based on ID within the same Excel file
def match_ids_within_sheet(file_path):
    xls = pd.ExcelFile(file_path)
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')

    # Merge dataframes on the ID column
    merged_df = pd.merge(df1, df2, on='ID', how='inner')

    return merged_df[['UUID', 'ScopusID']]

# Function to save matched results to a new Excel file
def save_matched_results(matched_data):
    matched_data.to_excel("matched_results.xlsx", index=False)

# Create a Tkinter window
root = tk.Tk()
root.title("Excel Sheet Matching Tool")
root.configure(bg='orange')

# Function to handle the matching process
def match_ids():
    file_path = filedialog.askopenfilename(title="Select Excel file with two sheets")
    if file_path:
        matched_data = match_ids_within_sheet(file_path)
        save_matched_results(matched_data)
        messagebox.showinfo("Matching Complete", "Matched results saved to matched_results.xlsx")
    else:
        messagebox.showinfo("No File Selected", "Please select an Excel file.")

# Create labels
label = tk.Label(root, text="Excel Sheet Matching Tool", font=("Arial", 14, "bold"), bg='orange', fg='white')
label.pack(pady=10)

# Create a button to trigger the matching process
match_button = tk.Button(root, text="Match IDs", command=match_ids, padx=20, pady=10, bg="white", fg="orange")
match_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()