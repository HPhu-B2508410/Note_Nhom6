# app.py (v0.1)
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

class NoteKeeperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NoteKeeper - Ứng dụng Ghi chú (v0.1)")
        self.root.geometry("900x550")

        style = tb.Style(theme="cosmo")

        top_frame = ttk.Frame(self.root)
        top_frame.pack(fill="x", pady=10, padx=10)

        title_label = ttk.Label(top_frame, text="📒 NoteKeeper", font=("Segoe UI", 20, "bold"))
        title_label.pack(side="left")

        btn_add = ttk.Button(top_frame, text="➕ Thêm ghi chú", bootstyle="success")
        btn_add.pack(side="right", padx=5)

        btn_exit = ttk.Button(top_frame, text="Thoát", bootstyle="danger", command=self.root.quit)
        btn_exit.pack(side="right")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        left_frame = ttk.Labelframe(main_frame, text="Danh sách ghi chú", padding=10)
        left_frame.pack(side="left", fill="y", padx=10)

        self.note_list = tk.Listbox(left_frame, height=25, width=35, font=("Segoe UI", 11))
        self.note_list.pack(side="left", fill="y")

        scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=self.note_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.note_list.config(yscrollcommand=scrollbar.set)

        right_frame = ttk.Labelframe(main_frame, text="Chi tiết ghi chú", padding=10)
        right_frame.pack(side="right", fill="both", expand=True)

        ttk.Label(right_frame, text="Tiêu đề:", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.entry_title = ttk.Entry(right_frame)
        self.entry_title.pack(fill="x", pady=5)

        ttk.Label(right_frame, text="Nội dung:", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        self.text_body = tk.Text(right_frame, height=15, font=("Segoe UI", 11))
        self.text_body.pack(fill="both", expand=True)

        btn_frame = ttk.Frame(right_frame)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="💾 Lưu", bootstyle="primary").pack(side="left", padx=5)
        ttk.Button(btn_frame, text="🗑 Xóa", bootstyle="danger").pack(side="left", padx=5)
        ttk.Button(btn_frame, text="✏ Sửa", bootstyle="warning").pack(side="left", padx=5)

        status = ttk.Label(self.root, text="Phiên bản UI 0.1 | Sẵn sàng", bootstyle="secondary")
        status.pack(side="bottom", fill="x")

if __name__ == "__main__":
    root = tb.Window(themename="cosmo")
    app = NoteKeeperApp(root)
    root.mainloop()
