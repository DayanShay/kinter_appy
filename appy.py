import tkinter as tk
from tkinter import messagebox

def get_client_from_crm(client_id):
    # Function to retrieve client information from CRM using the client ID
    # Replace this function with your own implementation
    if client_id == "":
        raise ValueError("Client ID cannot be empty")
    client_info = f"Client ID: {client_id} | Name: John Doe | Age: 30"
    return client_info

def send_info(entry_client_id, listbox):
    try:
        client_id = entry_client_id.get()
        client_info = get_client_from_crm(client_id)
        listbox.insert(tk.END, client_info)
        entry_client_id.delete(0, tk.END)
        listbox.selection_clear(0, tk.END)
    except ValueError as error:
        # Display the error message to the user
        error_message = str(error)
        messagebox.showerror("Error", error_message)

def send_client_to_aff(entry_client_id):
    try:
        client_id = entry_client_id.get()
        # Implement sending the client to affiliate here
        messagebox.showinfo("Sent to Aff", f"Client ID: {client_id} sent to affiliate successfully")
        entry_client_id.delete(0, tk.END)
    except ValueError as error:
        # Display the error message to the user
        error_message = str(error)
        messagebox.showerror("Error", error_message)

def create_gui():
    window = tk.Tk()
    window.title("Information Form")
    window.geometry("400x400")
    window.resizable(False, False)  # Set window to not resizable

    label_client_id = tk.Label(window, text="Client ID:")
    label_client_id.grid(row=0, column=0, padx=10, pady=10)

    entry_client_id = tk.Entry(window)
    entry_client_id.grid(row=0, column=1, padx=10, pady=10)
    entry_client_id.focus_set()

    button_send_to_aff = tk.Button(window, text="Send Client to Aff", command=lambda: send_client_to_aff(entry_client_id))
    button_send_to_aff.grid(row=1, column=0, padx=10, pady=10)

    button_get_info = tk.Button(window, text="Get Client to List", command=lambda: send_info(entry_client_id, listbox))
    button_get_info.grid(row=0, column=2, padx=10, pady=10)

    listbox = tk.Listbox(window, width=300, height=300)
    listbox.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Configure row and column properties
    window.grid_rowconfigure(2, weight=1)  # Allow the listbox to expand vertically
    window.grid_columnconfigure(0, weight=1)  # Allow the listbox to expand horizontally
    window.grid_columnconfigure(1, weight=1)  # Allow the listbox to expand horizontally
    window.grid_columnconfigure(2, weight=1)  # Allow the listbox to expand horizontally

    window.mainloop()

if __name__ == "__main__":
    create_gui()
