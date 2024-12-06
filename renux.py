import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox


def backup_packages():
    """Backup the list of installed packages."""
    output_file = filedialog.asksaveasfilename(
        title="Save Backup File",
        defaultextension=".list",
        filetypes=[("List files", "*.list"), ("All files", "*.*")],
    )
    if not output_file:
        return

    try:
        subprocess.run(
            ["dpkg", "--get-selections"],
            stdout=open(output_file, "w"),
            check=True,
        )
        messagebox.showinfo("Success", f"Backup completed successfully!\nFile: {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Error during backup: {e}")


def restore_packages():
    """Restore packages from a backup file."""
    input_file = filedialog.askopenfilename(
        title="Open Backup File",
        filetypes=[("List files", "*.list"), ("All files", "*.*")],
    )
    if not input_file or not os.path.exists(input_file):
        messagebox.showerror("Error", "No valid file selected.")
        return

    try:
        # Set package selections
        subprocess.run(
            ["sudo", "dpkg", "--set-selections"],
            stdin=open(input_file, "r"),
            check=True,
        )
        # Install selected packages
        subprocess.run(
            ["sudo", "apt-get", "dselect-upgrade", "-y"],
            check=True,
        )
        messagebox.showinfo("Success", "Restore completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error during restore: {e}")


def create_gui():
    """Create the GUI for the application."""
    root = tk.Tk()
    root.title("Ubuntu Package Backup and Restore")

    # Set window size
    root.geometry("400x200")

    # Create buttons
    backup_button = tk.Button(
        root, text="Backup Installed Packages", command=backup_packages, width=30, height=2
    )
    restore_button = tk.Button(
        root, text="Restore Packages from Backup", command=restore_packages, width=30, height=2
    )
    exit_button = tk.Button(root, text="Exit", command=root.quit, width=30, height=2)

    # Layout the buttons
    backup_button.pack(pady=10)
    restore_button.pack(pady=10)
    exit_button.pack(pady=10)

    # Run the Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    create_gui()
