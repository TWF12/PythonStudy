import tkinter as tk
from time import sleep
from tkinter import ttk, messagebox, filedialog
import json
import copy
import os
import re


class BankerAlgorithm:
    def __init__(self):
        self.reset()

    def reset(self):
        self.resource_types_count = 0  # 资源种类数
        self.process_count = 0  # 进程数
        self.resources = []  # 各类资源的初始数量
        self.Available = []  # 可用资源向量
        self.Max = []  # 最大需求矩阵
        self.Allocation = []  # 分配矩阵
        self.Need = []  # 需求矩阵
        self.process_names = []  # 进程名称列表

    def initialize_system(self, available, resources):
        self.resource_types_count = len(available)
        self.resources = resources.copy()
        self.Available = available.copy()

    def check_add_process_data(self, name, max, allocation):
        if self.resource_types_count == 0:
            raise ValueError("系统资源未初始化")
        if not name:
            raise ValueError("进程名称不能为空")
        if name in self.process_names:
            raise ValueError(f"进程{name}已存在")
        if len(max) != self.resource_types_count or len(allocation) != self.resource_types_count:
            raise ValueError(f"max和allocation的长度必须为{self.resource_types_count}")
        for i in range(self.resource_types_count):
            if max[i] < 0 or allocation[i] < 0 or allocation[i] > max[i] or allocation[i] > self.Available[i]:
                resource_name = chr(65 + i)  # 资源名称
                raise ValueError(
                    f"资源{resource_name}的max和allocation必须是非负数且allocation不能大于max,allocation不能大于available")

    def check_request_resources_data(self, process_name, request):
        if self.process_count == 0:
            raise ValueError(f"系统中无进程, 请先添加进程")
        if not process_name:
            raise ValueError("进程名称不能为空")
        if process_name not in self.process_names:
            raise ValueError(f"进程{process_name}不存在")
        if len(request) != self.resource_types_count:
            raise ValueError(f"request的长度必须为{self.resource_types_count}")
        process_index = self.process_names.index(process_name)  # 进程索引
        for i in range(self.resource_types_count):
            if request[i] < 0 or request[i] > self.Need[process_index][i] or request[i] > self.Available[i]:
                resource_name = chr(65 + i)
                raise ValueError(
                    f"资源{resource_name}的request必须是非负数且request不能大于need, request不能大于available")

    def _check_safety(self, available, allocation, need):
        # 创建副本并初始化Finish
        Work = available.copy()
        Finish = [False] * self.process_count

        # 进程索引列表
        process_index_list = list(range(self.process_count))

        # 排序策略：Need数由小到大，Need数相同按序号由小到大
        process_index_list.sort(key=lambda index: (
            sum(need[index]),  # Need数总和作为主要排序依据
            index  # 进程索引作为次要排序依据
        ))

        safe_sequence = []

        # 尝试寻找安全序列
        for _ in range(self.process_count):
            found = False
            for i in process_index_list:
                if not Finish[i]:
                    # 检查进程i的Need是否小于等于Work
                    if all(need[i][j] <= Work[j] for j in range(self.resource_types_count)):
                        # 模拟进程完成并释放全部资源
                        for k in range(self.resource_types_count):
                            Work[k] += allocation[i][k]
                        Finish[i] = True
                        safe_sequence.append(self.process_names[i])
                        found = True
                        break

            if not found and not all(Finish):
                return False, []
        return True, safe_sequence

    def add_process(self, name, max, allocation):
        # 数据合法性验证
        self.check_add_process_data(name, max, allocation)
        # 计算对各资源的需求
        need = [max[i] - allocation[i] for i in range(self.resource_types_count)]
        # 添加进程
        self.process_names.append(name)
        self.Max.append(max.copy())
        self.Allocation.append(allocation.copy())
        self.Need.append(need)

        # 更新Available和process_count
        for i in range(self.resource_types_count):
            self.Available[i] -= allocation[i]
        self.process_count += 1

        return True

    def request_resources(self, process_name, request):
        # 数据合法性验证
        self.check_request_resources_data(process_name, request)

        process_index = self.process_names.index(process_name)  # 进程索引

        # 创建副本
        temp_available = self.Available.copy()
        temp_allocation = copy.deepcopy(self.Allocation)
        temp_need = copy.deepcopy(self.Need)

        # 模拟分配
        for i in range(self.resource_types_count):
            temp_available[i] -= request[i]
            temp_allocation[process_index][i] += request[i]
            temp_need[process_index][i] -= request[i]

        # 检查分配后是否安全
        is_safe, safe_sequence = self._check_safety(temp_available, temp_allocation, temp_need)

        if is_safe:
            # 正式分配
            for i in range(self.resource_types_count):
                self.Available[i] -= request[i]
                self.Allocation[process_index][i] += request[i]
                self.Need[process_index][i] -= request[i]

            # 检查进程是否完成
            if all(self.Need[process_index][i] == 0 for i in range(self.resource_types_count)):
                # 释放进程占用的所有资源
                for i in range(self.resource_types_count):
                    self.Available[i] += self.Allocation[process_index][i]
                    self.Allocation[process_index][i] = 0
                return True, f"进程{self.process_names[process_index]}完成并释放所有资源"

            return True, "分配成功, 系统仍处于安全状态"
        else:
            return False, "分配失败, 分配会导致系统进入不安全状态"

    def check_safety(self):
        return self._check_safety(self.Available, self.Allocation, self.Need)

    def get_system_state(self):
        return {
            "resource_types_count": self.resource_types_count,
            "process_count": self.process_count,
            "resources": self.resources,
            "Available": self.Available,
            "Aax": self.Max,
            "Allocation": self.Allocation,
            "Need": self.Need,
            "process_names": self.process_names
        }


class ResourceAllocationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("动态资源分配算法演示程序")  # 窗口标题
        self.root.geometry("1200x700")  # 窗口大小

        # 创建银行家算法的一个实例
        self.banker = BankerAlgorithm()

        # 创建界面
        self.create_widgets()

        # 初始化示例数据
        self.init_sample_data()

    def create_widgets(self):
        """创建界面组件"""
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(5, weight=1)

        # 标题
        title_label = ttk.Label(main_frame, text="动态资源分配算法演示程序",
                                font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        # 系统初始化区域
        init_frame = ttk.LabelFrame(main_frame, text="系统初始化", padding="10")
        init_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))

        # 资源设置
        ttk.Label(init_frame, text="资源种类数:").grid(row=0, column=0, padx=(0, 5))
        self.resource_count_var = tk.StringVar(value="3")
        resource_count_entry = ttk.Entry(init_frame, textvariable=self.resource_count_var, width=10)
        resource_count_entry.grid(row=0, column=1, padx=(0, 10))

        ttk.Label(init_frame, text="各类资源最大实例数 (逗号分隔):").grid(row=0, column=2, padx=(0, 5))
        self.resources_var = tk.StringVar(value="10,5,7")
        resources_entry = ttk.Entry(init_frame, textvariable=self.resources_var, width=20)
        resources_entry.grid(row=0, column=3, padx=(0, 10))

        ttk.Label(init_frame, text="初始可用资源 (逗号分隔):").grid(row=0, column=4, padx=(0, 5))
        self.Available_available_var = tk.StringVar(value="10,5,7")
        available_available_entry = ttk.Entry(init_frame, textvariable=self.Available_available_var, width=20)
        available_available_entry.grid(row=0, column=5, padx=(0, 10))

        init_button = ttk.Button(init_frame, text="初始化系统", command=self.initialize_system)
        init_button.grid(row=0, column=6, padx=(10, 0))

        # 文件操作区域
        file_frame = ttk.LabelFrame(main_frame, text="文件操作", padding="10")
        file_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Button(file_frame, text="从文件加载样例数据",
                   command=self.load_from_file).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(file_frame, text="保存当前状态到文件",
                   command=self.save_to_file).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(file_frame, text="重置系统",
                   command=self.reset_system).pack(side=tk.LEFT)

        # 进程管理区域
        process_frame = ttk.LabelFrame(main_frame, text="进程管理", padding="10")
        process_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(process_frame, text="进程名称:").grid(row=0, column=0, padx=(0, 5))
        self.process_name_var = tk.StringVar(value="P0")
        process_name_entry = ttk.Entry(process_frame, textvariable=self.process_name_var, width=10)
        process_name_entry.grid(row=0, column=1, padx=(0, 10))

        ttk.Label(process_frame, text="最大需求 (逗号分隔):").grid(row=0, column=2, padx=(0, 5))
        self.Max_var = tk.StringVar(value="7,5,3")
        max_entry = ttk.Entry(process_frame, textvariable=self.Max_var, width=15)
        max_entry.grid(row=0, column=3, padx=(0, 10))

        ttk.Label(process_frame, text="已分配 (逗号分隔):").grid(row=0, column=4, padx=(0, 5))
        self.Allocation_var = tk.StringVar(value="0,1,0")
        allocation_entry = ttk.Entry(process_frame, textvariable=self.Allocation_var, width=15)
        allocation_entry.grid(row=0, column=5, padx=(0, 10))

        add_process_button = ttk.Button(process_frame, text="添加进程", command=self.add_process)
        add_process_button.grid(row=0, column=6, padx=(10, 0))

        # 资源请求区域
        request_frame = ttk.LabelFrame(main_frame, text="资源请求", padding="10")
        request_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))

        ttk.Label(request_frame, text="选择进程:").grid(row=0, column=0, padx=(0, 5))
        self.process_var = tk.StringVar()
        self.process_combobox = ttk.Combobox(request_frame, textvariable=self.process_var, width=15)
        self.process_combobox.grid(row=0, column=1, padx=(0, 10))

        ttk.Label(request_frame, text="请求资源 (逗号分隔):").grid(row=0, column=2, padx=(0, 5))
        self.request_var = tk.StringVar(value="0,0,0")
        request_entry = ttk.Entry(request_frame, textvariable=self.request_var, width=15)
        request_entry.grid(row=0, column=3, padx=(0, 10))

        request_button = ttk.Button(request_frame, text="请求资源", command=self.request_resources)
        request_button.grid(row=0, column=4, padx=(10, 0))

        safety_button = ttk.Button(request_frame, text="安全性检查", command=self.check_safety)
        safety_button.grid(row=0, column=5, padx=(10, 0))

        # 系统状态显示区域
        state_frame = ttk.LabelFrame(main_frame, text="系统状态", padding="10")
        state_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))

        # 创建文本框显示系统状态
        self.state_text = tk.Text(state_frame, height=20, width=140)
        self.state_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # 添加滚动条
        scrollbar = ttk.Scrollbar(state_frame, orient=tk.VERTICAL, command=self.state_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.state_text.configure(yscrollcommand=scrollbar.set)

        # 配置网格权重
        state_frame.columnconfigure(0, weight=1)
        state_frame.rowconfigure(0, weight=1)

        # 状态栏
        self.status_var = tk.StringVar(value="就绪")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))

    def init_sample_data(self):
        """初始化示例数据"""
        # 创建示例数据文件
        sample_data = {
            "resource_types_count": 3,
            "resources": [10, 5, 7],
            "available": [10, 5, 7],
            "processes": [
                {"name": "P0", "max": [7, 5, 3], "allocation": [0, 1, 0]},
                {"name": "P1", "max": [3, 2, 2], "allocation": [2, 0, 0]},
                {"name": "P2", "max": [9, 0, 2], "allocation": [3, 0, 2]},
                {"name": "P3", "max": [2, 2, 2], "allocation": [2, 1, 1]},
                {"name": "P4", "max": [4, 3, 3], "allocation": [0, 0, 2]}
            ]
        }

        # 保存到文件
        with open("sample_data.json", "w") as f:
            json.dump(sample_data, f, indent=2)

        self.status_var.set("示例数据文件已创建: sample_data.json")

    def initialize_system(self):
        """初始化系统资源"""
        try:
            # 获取资源种类数
            resource_count = int(self.resource_count_var.get())
            if resource_count <= 0:
                raise ValueError("资源种类数必须为正整数")

            # 解析最大资源数
            resources_str = self.resources_var.get()
            resources = [int(x.strip()) for x in resources_str.split(",")]
            if len(resources) != resource_count:
                raise ValueError(f"最大资源数必须包含{resource_count}个值")

            # 解析可用资源
            available_str = self.Available_available_var.get()
            available = [int(x.strip()) for x in available_str.split(",")]
            if len(available) != resource_count:
                raise ValueError(f"可用资源必须包含{resource_count}个值")

            # 检查可用资源是否超过最大资源
            for i in range(resource_count):
                if available[i] > resources[i]:
                    raise ValueError(f"可用资源{i}不能超过最大资源{i}")

            # 初始化系统
            self.banker.initialize_system(available, resources)

            self.update_display()
            self.status_var.set(f"系统初始化成功: {resource_count}种资源，最大资源{resources}，可用资源{available}")

        except ValueError as e:
            messagebox.showerror("输入错误", str(e))

    def add_process(self):
        try:
            # 获取进程名称
            name = self.process_name_var.get()

            # 获取进程最大需求
            max_str = self.Max_var.get()
            max = [int(x.strip()) for x in re.split(r"[, ，]", max_str)]

            # 获取进程已分配资源
            allocation_str = self.Allocation_var.get()
            allocation = [int(x.strip()) for x in re.split(r"[, ，]", allocation_str)]

            # 数据合法性验证
            self.banker.check_add_process_data(name, max, allocation)

            # 添加进程
            self.banker.add_process(name, max, allocation)

            # 更新进程下拉列表
            self.update_process_combobox()

            self.update_display()
            self.status_var.set(f"进程{name}添加成功")

        except ValueError as e:
            messagebox.showerror("输入错误", str(e))

    def request_resources(self):
        try:
            # 获取请求资源的进程名称
            process_name = self.process_var.get()
            # 获取请求的各资源数量
            request_str = self.request_var.get()
            request = [int(x.strip()) for x in re.split(r"[, ，]", request_str)]

            # 数据合法性验证
            self.banker.check_request_resources_data(process_name, request)

            # 请求资源
            success, message = self.banker.request_resources(process_name, request)

            if success:
                # 如果进程完成，从下拉列表中移除
                if "完成" in message:
                    self.update_process_combobox()

                self.status_var.set(message)
            else:
                self.status_var.set(f"请求失败: {message}")

            self.update_display()

        except ValueError as e:
            messagebox.showerror("输入错误", str(e))

    def check_safety(self):
        """进行安全性检查"""
        try:
            if self.banker.process_count == 0:
                messagebox.showwarning("无进程", "请先添加进程")
                return

            is_safe, safe_sequence = self.banker.check_safety()

            if is_safe:
                message = f"系统处于安全状态\n安全序列: {safe_sequence}"
                messagebox.showinfo("安全性检查", message)
                self.status_var.set("系统处于安全状态")
            else:
                messagebox.showwarning("安全性检查", "系统处于不安全状态！")
                self.status_var.set("系统处于不安全状态")

        except Exception as e:
            messagebox.showerror("错误", f"安全性检查失败: {str(e)}")

    def load_from_file(self):
        """从文件加载数据"""
        try:
            file_path = filedialog.askopenfilename(
                title="选择数据文件",
                filetypes=[("JSON文件", "*.json"), ("所有文件", "*.*")]
            )

            if not file_path:
                return

            with open(file_path, "r") as f:
                data = json.load(f)

            # 重置系统
            self.banker.reset()

            # 初始化系统资源
            self.banker.initialize_system(data["available"], data["resources"])

            # 添加进程
            for process in data["processes"]:
                self.banker.add_process(
                    process["name"],
                    process["max"],
                    process["allocation"]
                )

            # 更新界面
            self.resource_count_var.set(str(data["resource_types_count"]))
            self.resources_var.set(",".join(str(x) for x in data["resources"]))
            self.Available_available_var.set(",".join(str(x) for x in data["available"]))

            self.update_process_combobox()
            self.update_display()

            self.status_var.set(f"从文件加载成功: {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("加载错误", f"加载文件失败: {str(e)}")

    def save_to_file(self):
        """保存当前状态到文件"""
        try:
            file_path = filedialog.asksaveasfilename(
                title="保存数据文件",
                defaultextension=".json",
                filetypes=[("JSON文件", "*.json"), ("所有文件", "*.*")]
            )

            if not file_path:
                return

            # 获取系统状态
            state = self.banker.get_system_state()

            # 准备数据
            data = {
                "resource_types_count": state["resource_types_count"],
                "resources": state["resources"],
                "available": state["available"],
                "processes": []
            }

            for i in range(state["process_count"]):
                process_data = {
                    "name": state["process_names"][i],
                    "max": state["max"][i],
                    "allocation": state["allocation"][i]
                }
                data["processes"].append(process_data)

            # 保存到文件
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2)

            self.status_var.set(f"状态保存成功: {os.path.basename(file_path)}")

        except Exception as e:
            messagebox.showerror("保存错误", f"保存文件失败: {str(e)}")

    def reset_system(self):
        """重置系统"""
        self.banker.reset()
        self.process_combobox.set("")
        self.update_display()
        self.status_var.set("系统已重置")

    def update_process_combobox(self):
        self.process_combobox["values"] = self.banker.process_names
        if self.banker.process_names:
            self.process_combobox.current(0)

    def update_display(self):
        state = self.banker.get_system_state()  # 获取系统状态
        self.state_text.delete(1.0, tk.END)

        # 显示资源信息
        self.state_text.insert(tk.END, "=" * 80 + "\n")
        self.state_text.insert(tk.END, "系统资源状态\n")
        self.state_text.insert(tk.END, "=" * 80 + "\n\n")

        self.state_text.insert(tk.END, f"资源种类数: {state['resource_types_count']}\n")
        self.state_text.insert(tk.END, f"最大资源实例: {state['resources']}\n")
        self.state_text.insert(tk.END, f"当前可用资源: {state['available']}\n\n")

        # 显示进程信息
        if state["process_count"] > 0:
            self.state_text.insert(tk.END, "=" * 80 + "\n")
            self.state_text.insert(tk.END, "进程状态\n")
            self.state_text.insert(tk.END, "=" * 80 + "\n\n")

            # 表头
            header = f"{'进程':<10} {'最大需求(Max)':<30} {'已分配(Allocation)':<30} {'需求(Need)':<30} {'完成状态':<10}\n"
            self.state_text.insert(tk.END, header)
            self.state_text.insert(tk.END, "-" * 110 + "\n")

            # 进程行
            for i in range(state["process_count"]):
                process_name = state["process_names"][i]
                max_str = str(state["max"][i])
                allocation_str = str(state["allocation"][i])
                need_str = str(state["need"][i])

                # 判断进程是否完成
                is_finished = all(need == 0 for need in state["need"][i])
                finish_status = "完成" if is_finished else "未完成"

                row = f"{process_name:<10} {max_str:<30} {allocation_str:<30} {need_str:<30} {finish_status:<10}\n"
                self.state_text.insert(tk.END, row)

            self.state_text.insert(tk.END, "\n")

        # 自动滚动到顶部
        self.state_text.see(1.0)


def main():
    """主函数"""
    root = tk.Tk()
    app = ResourceAllocationApp(root)
    root.mainloop()




if __name__ == "__main__":
    main()
