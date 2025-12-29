import ctypes
import datetime
import tkinter as tk
from tkinter import messagebox

class SystemDateChanger:
    def __init__(self, root):
        self.root = root
        self.root.title("系统日期增加器")
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        
        # 设置中文字体支持
        self.setup_fonts()
        
        # 创建界面元素
        self.create_widgets()
        
    def setup_fonts(self):
        # 确保中文显示正常
        default_font = ('SimHei', 10)
        self.root.option_add("*Font", default_font)
        
    def create_widgets(self):
        # 当前日期显示
        self.current_date_label = tk.Label(self.root, text="当前系统日期: " + self.get_current_date())
        self.current_date_label.pack(pady=10)
        
        # 增加日期按钮
        self.increment_btn = tk.Button(
            self.root, 
            text="增加1天", 
            command=self.increment_date,
            width=15,
            height=2,
            font=('SimHei', 12)
        )
        self.increment_btn.pack(pady=20)
        
    def get_current_date(self):
        """获取当前系统日期"""
        now = datetime.datetime.now()
        return now.strftime("%Y年%m月%d日 %H:%M:%S")
    
    def update_date_label(self):
        """更新日期显示"""
        self.current_date_label.config(text="当前系统日期: " + self.get_current_date())
    
    def increment_date(self):
        """将系统日期增加1天（修正时区问题）"""
        try:
            # 获取当前本地时间
            now = datetime.datetime.now()
            
            # 计算明天的日期（精确增加1天）
            tomorrow = now + datetime.timedelta(days=1)
            
            # 调用Windows API设置系统时间
            # SYSTEMTIME结构定义
            class SYSTEMTIME(ctypes.Structure):
                _fields_ = [
                    ("wYear", ctypes.c_uint16),
                    ("wMonth", ctypes.c_uint16),
                    ("wDayOfWeek", ctypes.c_uint16),
                    ("wDay", ctypes.c_uint16),
                    ("wHour", ctypes.c_uint16),
                    ("wMinute", ctypes.c_uint16),
                    ("wSecond", ctypes.c_uint16),
                    ("wMilliseconds", ctypes.c_uint16)
                ]
            
            # 填充SYSTEMTIME结构（使用本地时间）
            st = SYSTEMTIME()
            st.wYear = tomorrow.year
            st.wMonth = tomorrow.month
            st.wDay = tomorrow.day
            st.wHour = now.hour  # 保持当前小时
            st.wMinute = now.minute  # 保持当前分钟
            st.wSecond = now.second  # 保持当前秒数
            st.wMilliseconds = now.microsecond // 1000  # 保持当前毫秒
            
            # 关键修正：使用SetLocalTime代替SetSystemTime
            # SetLocalTime直接操作本地时间，不会进行时区转换
            kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
            result = kernel32.SetLocalTime(ctypes.byref(st))  # 这里修改了函数名
            
            if result == 0:
                # 获取错误信息
                error_code = ctypes.get_last_error()
                raise ctypes.WinError(error_code)
            
            # 更新日期显示
            self.update_date_label()
            messagebox.showinfo("成功", f"系统日期已更新为: {tomorrow.strftime('%Y年%m月%d日 %H:%M:%S')}")
            
        except Exception as e:
            messagebox.showerror("错误", f"无法修改系统日期: {str(e)}\n请确保以管理员身份运行程序。")

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemDateChanger(root)
    root.mainloop()
    