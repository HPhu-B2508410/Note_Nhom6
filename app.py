import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb


notes = []  # danh sách ghi chú


class NoteKeeperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NoteKeeper - v0.2")
        self.root.geometry("950x600")

        tb.Style(theme="cosmo")

        self.current_index = None
        self.is_loading_note = False  # tránh auto-save khi đang load note

        self.build_header()
        self.build_layout()
        self.build_status()

        # auto-save khi nhập
        self.entry_title.bind("<KeyRelease>", self.auto_save)
        self.text_body.bind("<KeyRelease>", self.auto_save)

        self.note_list.bind("<<ListboxSelect>>", self.load_note)

    # -----------------------------------------
    # UI
    # -----------------------------------------
    def build_header(self):
        top = ttk.Frame(self.root)
        top.pack(fill="x", padx=10, pady=8)

        ttk.Label(top, text="📒 NoteKeeper", font=("Segoe UI", 22, "bold")).pack(side="left")

        ttk.Button(top, text="➕ Ghi chú mới", bootstyle="success", command=self.create_note).pack(side="right", padx=6)
        ttk.Button(top, text="🗑 Xóa", bootstyle="danger", command=self.delete_note).pack(side="right")

    def build_layout(self):
        main = ttk.Frame(self.root)
        main.pack(fill="both", expand=True, padx=10, pady=10)

        # List trái
        left = ttk.Labelframe(main, text="Danh sách ghi chú", padding=8)
        left.pack(side="left", fill="y", padx=5)

        self.note_list = tk.Listbox(left, width=35, height=28, font=("Segoe UI", 11))
        self.note_list.pack(side="left", fill="y")

        scrollbar = ttk.Scrollbar(left, command=self.note_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.note_list.config(yscrollcommand=scrollbar.set)

        # Chi tiết phải
        right = ttk.Labelframe(main, text="Chi tiết ghi chú", padding=8)
        right.pack(side="right", fill="both", expand=True)

        ttk.Label(right, text="Tiêu đề:", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        self.entry_title = ttk.Entry(right, font=("Segoe UI", 12))
        self.entry_title.pack(fill="x", pady=5)

        ttk.Label(right, text="Nội dung:", font=("Segoe UI", 12, "bold")).pack(anchor="w")
        self.text_body = tk.Text(right, font=("Segoe UI", 11))
        self.text_body.pack(fill="both", expand=True)

    def build_status(self):
        self.status = ttk.Label(self.root, text="Sẵn sàng", bootstyle="secondary")
        self.status.pack(fill="x", side="bottom")

    # -----------------------------------------
    # LOGIC
    # -----------------------------------------
    def refresh_list(self):
        self.note_list.delete(0, tk.END)
        for note in notes:
            preview = (note["body"][:20] + "...") if len(note["body"]) > 20 else note["body"]
            title = note["title"] if note["title"] else "(Không có tiêu đề)"
            self.note_list.insert(tk.END, f"{title}")

    def load_note(self, e=None):
        if not self.note_list.curselection():
            return

        self.is_loading_note = True  # ngăn auto-save lúc load

        index = self.note_list.curselection()[0]
        self.current_index = index

        note = notes[index]

        self.entry_title.delete(0, tk.END)
        self.entry_title.insert(0, note["title"])

        self.text_body.delete("1.0", tk.END)
        self.text_body.insert("1.0", note["body"])

        self.status.config(text=f"Đã tải ghi chú #{index + 1}")

        self.is_loading_note = False

    def create_note(self):
        notes.append({"title": "", "body": ""})
        self.refresh_list()

        # auto chọn note mới
        self.note_list.select_set(len(notes) - 1)
        self.load_note()

        self.status.config(text="Đã tạo ghi chú mới")

    def auto_save(self, event=None):
        if self.is_loading_note:
            return

        if self.current_index is None:
            return

        notes[self.current_index]["title"] = self.entry_title.get()
        notes[self.current_index]["body"] = self.text_body.get("1.0", tk.END).strip()

        self.refresh_list()
        self.status.config(text="Đã tự động lưu")

    def delete_note(self):
        if self.current_index is None:
            return

        notes.pop(self.current_index)
        self.current_index = None

        self.entry_title.delete(0, tk.END)
        self.text_body.delete("1.0", tk.END)

        self.refresh_list()

        self.status.config(text="Đã xóa ghi chú")


# -----------------------------------------
# RUN APP
# -----------------------------------------
if __name__ == "__main__":
    root = tb.Window(themename="cosmo")
    NoteKeeperApp(root)
    root.mainloop()
