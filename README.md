# NoteKeeper

**NoteKeeper** là một ứng dụng ghi chú đơn giản nhưng hiệu quả, được phát triển với giao diện GUI thân thiện. Dự án này bao gồm hai phiên bản chính:

- **v0.1** – Tao giao dien NoteKeeper
- **v0.2** – Thêm tính năng Thêm/Xóa/Sửa ghi chú
- **v0.3** – Release chính thức với tính năng auto-save

---

##  Công nghệ sử dụng

- Python 3.13
- Tkinter + ttkbootstrap (GUI hiện đại)
- JSON (v0.3) để lưu dữ liệu
- Git & GitHub để quản lý phiên bản
- Cross-platform: Windows, macOS, Linux

---

##  Cấu trúc thư mục
NoteKeeper/
│
├─ app.py # Main application code
├─ notes.json # Dữ liệu ghi chú (v0.3)
├─ .gitignore # Bỏ qua các file tạm
└─ README.md # File hướng dẫn

---


---

##  Phiên bản v0.1 – Giao dien co ban

**Thời gian phát triển:** Tuần 1  

**Chức năng:**

1. Tạo giao diện chính bằng Tkinter + ttkbootstrap  
2. Danh sách ghi chú bên trái  
3. Khung hiển thị chi tiết bên phải  
4. Nút Thêm, Lưu, Xóa, Sửa (chưa hoạt động)  

**Hạn chế:**  
- Chưa có logic thêm/xóa/sửa thực tế  
- Chưa lưu dữ liệu  


---

##  Phiên bản v0.2 – Lưu trong RAM

**Thời gian phát triển:** Tuần 1–2  

**Chức năng:**

1. Thêm ghi chú mới  
2. Xóa ghi chú  
3. Sửa ghi chú (cập nhật trực tiếp trong GUI)  
4. Danh sách note hiển thị tiêu đề + preview ngắn  
5. UI tương tác dễ sử dụng, tối ưu layout  

**Hạn chế:**  
- Chưa lưu dữ liệu ra file → khi tắt app, ghi chú sẽ mất


---

## Phiên bản v0.3 – Release Final

**Thời gian phát triển:** Tuần 3  

**Chức năng chính:**

1. **Tất cả chức năng v0.2** 
2. **Lưu và tải dữ liệu tự động** qua file `notes.json`  
3. **Auto-save** khi chỉnh sửa tiêu đề hoặc nội dung  
4. Tự tạo `notes.json` nếu chưa tồn tại  
5. Preview danh sách note ngắn gọn, dễ nhìn  
