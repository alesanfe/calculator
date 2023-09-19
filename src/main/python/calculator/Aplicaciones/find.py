import os
from Tool import src as M
import tkinter as tk


class FileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Search App")

        self.possibilities = M.Text("", 13)

        self.varOption = tk.StringVar()
        self.fileName = tk.StringVar()

        self.entry_widget = EntryWidget(root, self.fileName)
        self.format_selector = FormatSelector(root, self.varOption, self.print_file_type)
        self.search_button = SearchButton(root, self.search_file)
        self.result_label = ResultLabel(root)

    def search_file(self):
        ext = self.varOption.get()
        file_name = self.fileName.get()
        program = f"{file_name}.{ext}"

        for used_direction in self.possibilities.Return_Text.split(","):
            if program in used_direction:
                self.result_label.display_direction(used_direction)
                return

        for root_directory, _, files in os.walk("/"):
            for file in files:
                if file == program:
                    direction = os.path.join(root_directory, file)
                    self.possibilities.Append_Text(f"{direction},")
                    self.result_label.display_direction(direction)
                    return

    def print_file_type(self):
        file_type = self.varOption.get()
        file_name = self.fileName.get()
        label_text = f"The file to search is '{file_name}.{file_type}.'"
        self.result_label.set_text(label_text)


class EntryWidget:
    def __init__(self, root, text_variable):
        self.entry = tk.Entry(
            root,
            textvariable=text_variable,
            font=("Calculator", 24),
            relief=tk.RAISED,
            justify=tk.RIGHT,
            borderwidth=0
        )
        self.entry.grid(row=1, column=1, padx=10, pady=10, columnspan=3, sticky="nsew")
        self.entry.config(background="black", fg="#03f943", justify="right")


class FormatSelector:
    def __init__(self, root, var_option, command):
        self.varOption = var_option
        text_label = tk.Label(root, text="Choose the format:")
        text_label.grid(row=2, column=1, columnspan=3)

        file_types = ["exe", "png", "pdf", "mp4", "py", "docx"]
        row, col = 3, 1

        for file_type in file_types:
            tk.Radiobutton(
                root,
                text=file_type,
                variable=self.varOption,
                value=file_type,
                command=command
            ).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 1
                row += 1


class SearchButton:
    def __init__(self, root, command):
        tk.Button(
            root,
            text="Search",
            width=3,
            command=command
        ).grid(row=5, column=2, sticky="nsew")


class ResultLabel:
    def __init__(self, root):
        self.label = tk.Label(root)
        self.label.grid(row=0, column=1)

    def display_direction(self, direction):
        tk.Label(root, text=direction).grid(row=6, column=1, columnspan=3)

    def set_text(self, text):
        self.label.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearchApp(root)
    root.mainloop()

