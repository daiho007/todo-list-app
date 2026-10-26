tasks = []
"""TS. Trần Văn Long, Khoa Tin học, Trường Đại học Sư phạm, Đại học Huế

NHẬP MÔN CÔNG NGHỆ PHẦN MỀM| HƯỚNG DẪN THỰC HÀNH 3"""
def add_task(task_name):
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
add_task("Học bài Git và GitHub")
add_task("Làm bài tập thực hành ở nhà")