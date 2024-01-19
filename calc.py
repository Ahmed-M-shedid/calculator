import tkinter as tk

def convert_to_result():
    try:
        parts_value = float(entry_parts.get())
        num_pages_value = float(entry_num_pages.get())

        result_parts = parts_value * 10
        result_pages = num_pages_value * 0.5  # Adjust the multiplier as needed
        book_cost = result_parts + result_pages

        result_label.config(text=f"Book Cost: {book_cost}")
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Ketabology Calulator")

# Create and place widgets
label_num_pages = tk.Label(root, text="No. of  pages:")
label_num_pages.pack(pady=10)

entry_num_pages = tk.Entry(root)
entry_num_pages.pack(pady=10)

label_parts = tk.Label(root, text="No. of Parts:")
label_parts.pack(pady=10)

entry_parts = tk.Entry(root)
entry_parts.pack(pady=10)



convert_button = tk.Button(root, text="Calculate", command=convert_to_result)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="Book Cost:")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
