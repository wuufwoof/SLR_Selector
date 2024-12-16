import tkinter as tk
from tkinter import messagebox
import webbrowser
import requests

current_version = "1.1.5"  # 用你的當前版本替換

# Function to go back to the main menu
def show_main_menu():
    selection_frame.pack_forget()
    settings_frame.pack_forget()
    main_menu_frame.pack(pady=10)

# Function to handle the back button
def back_to_menu():
    show_main_menu()

class Champion:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

# Define the champions with their respective classes
champions = [
    Champion("刀鋒偤長", ["普攻", "暴擊"]),
    Champion("白虎射手", ["普攻", "回復"]),
    Champion("毒龍騎士", ["普攻", "毒"]),
    Champion("冰雪魔靈", ["普攻", "回復", "冰", "易傷", "護盾"]),
    Champion("隱匿之刃", ["閃避", "回復"]),
    Champion("惡魔之影", ["閃避", "暴擊", "回復", "生命"]),
    Champion("魅影刺客", ["閃避", "毒"]),
    Champion("破魔者", ["閃避", "回復"]),
    Champion("森林遊俠", ["閃避", "回復", "大招"]),
    Champion("狂暴斧王", ["暴擊", "回復", "大招"]),
    Champion("極寒掌控者", ["暴擊", "冰", "大招"]),
    Champion("雙頭魔法師", ["暴擊", "大招"]),
    Champion("覓血蛛王", ["暴擊", "毒"]),
    Champion("雷神", ["生命", "回復", "大招", "毒"]),
    Champion("深海巨人", ["生命", "回復", "毒", "冰"]),
    Champion("熊貓武士", ["回復", "毒", "冰"]),
    Champion("精靈牧師", ["精靈", "回復"]),
    Champion("神秘法師", ["大招", "回復", "生命", "精靈"]),
    Champion("劇毒巫師", ["毒", "回復", "精靈", "冰"]),
    Champion("瘟疫術士", ["毒", "回復"]),
    Champion("皇家騎士", ["護盾", "毒"]),
    Champion("部落勇士", ["護盾", "毒"]),
    Champion("混亂使徒", ["易傷"]),
    Champion("星界法師", ["易傷", "大招"]),
    Champion("娜迦女王", ["冰", "易傷"]),
    Champion("叢林先知", ["精靈"]),
    Champion("混亂魔王", ["精靈", "易傷"]),
    Champion("樹精守衛", ["精靈", "護盾", "大招"]),
    Champion("辣椒射手", ["怒氣", "易傷", "大招"]),
    Champion("狂怒法師", ["怒氣", "暴擊"])
]

# Function to get the favorable champions based on banned classes
def get_favorable_champions(banned_classes):
    favorable_champions = []
    for champion in champions:
        if not any(banned_class in champion.classes for banned_class in banned_classes):
            favorable_champions.append(champion)
    return favorable_champions

# Function to handle the button click to show champion classes
def show_classes(champion):
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"{champion.name} 流派: {', '.join(champion.classes)}")

# Function to handle the button click for showing champions
def show_champions():
    banned_classes = [cls for cls in class_vars if class_vars[cls].get()]
    favorable_champions = get_favorable_champions(banned_classes)
    
    # Clear the previous results
    result_text.delete(1.0, tk.END)
    
    # Clear previous buttons
    for widget in champion_frame.winfo_children():
        widget.destroy()

    if favorable_champions:
        for champion in favorable_champions:
            button = tk.Button(champion_frame, text=champion.name, command=lambda c=champion: show_classes(c))
            button.pack(pady=5)
    else:
        result_text.insert(tk.END, "Reroll!")

# Function to reset selections
def reset_selection():
    for var in class_vars.values():
        var.set(False)
    
    result_text.delete(1.0, tk.END)
    for widget in champion_frame.winfo_children():
        widget.destroy()

# Function to switch to the champion selection screen
def show_selection_screen():
    main_menu_frame.pack_forget()
    selection_frame.pack(pady=10)

# Function to go back to the main menu
def show_main_menu():
    selection_frame.pack_forget()
    settings_frame.pack_forget()
    main_menu_frame.pack(pady=10)

# Function to toggle light/dark mode
def toggle_mode(mode):
    if mode == "dark":
        root.tk_setPalette(background='dimgrey')
        root.option_add('*Foreground', 'white')
        root.option_add('*Background', 'dimgrey')

        # Update specific widgets for dark mode
        for widget in root.winfo_children():
            widget.config(bg='dimgrey')  # Set background to black
            if isinstance(widget, (tk.Button, tk.Label, tk.Text)):
                widget.config(fg='white')  # Set text color to white

            # For Text widget, set specific background
            if isinstance(widget, tk.Text):
                widget.config(bg='dimgrey', fg='white')
    else:
        root.tk_setPalette(background='whitesmoke')
        root.option_add('*Foreground', 'black')
        root.option_add('*Background', 'whitesmoke')

        # Update specific widgets for light mode
        for widget in root.winfo_children():
            widget.config(bg='whitesmoke')  # Set background to white
            if isinstance(widget, (tk.Button, tk.Label, tk.Text)):
                widget.config(fg='black')  # Set text color to black
            
            # For Text widget, set specific background
            if isinstance(widget, tk.Text):
                widget.config(bg='whitesmoke', fg='black')

# Function to open URLs
def open_url(url):
    webbrowser.open(url)

# Function to check for version updates
import requests
import os

def download_patch(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        messagebox.showinfo("下載完成", f"補丁已下載到 {filename}")
    else:
        messagebox.showerror("錯誤", "無法下載補丁，請稍後再試。")

import requests
import os

def show_update_dialog(latest_version):
    update_window = tk.Toplevel(root)
    update_window.title("更新可用")
    
    tk.Label(update_window, text=f"發現新版本 {latest_version}").pack(pady=10)
    tk.Button(update_window, text="前往更新頁面", command=lambda: open_url("https://github.com/wuufwoof/SLR_Selector/releases/")).pack(pady=5)
    tk.Button(update_window, text="關閉", command=update_window.destroy).pack(pady=5)

def check_for_updates():
    try:
        response = requests.get("https://api.github.com/repos/wuufwoof/SLR_Selector/releases/latest")
        if response.status_code == 200:
            data = response.json()
            latest_version = data.get('tag_name')
            current_version = "1.1.0"  # Replace with your current version
            
            if latest_version and latest_version != current_version:
                show_update_dialog(latest_version)
            else:
                messagebox.showinfo("版本更新", "這已是最新版本")
        else:
            messagebox.showerror("錯誤", f"API 請求失敗，狀態碼：{response.status_code}")
    except Exception as e:
        messagebox.showerror("錯誤", f"無法檢查更新: {e}")

        tk.Button(update_window, text="關閉", command=update_window.destroy).pack(pady=5)

# Function to show settings options
def show_settings_screen():
    main_menu_frame.pack_forget()
    settings_frame.pack(pady=10)

# Set up the GUI window
root = tk.Tk()
root.title("英雄推薦器")

# Main menu frame
main_menu_frame = tk.Frame(root)
main_menu_frame.pack(pady=10)

# Buttons for main menu
tk.Button(main_menu_frame, text="推薦英雄", command=show_selection_screen).pack(pady=5)
tk.Button(main_menu_frame, text="設定", command=show_settings_screen).pack(pady=5)
tk.Button(main_menu_frame, text="官方Discord", command=lambda: open_url("https://discord.gg/PU9ZFHSBYD")).pack(pady=5)
tk.Button(main_menu_frame, text="官方Twitter", command=lambda: open_url("https://x.com/ZGGameStudio")).pack(pady=5)

# Selection frame
selection_frame = tk.Frame(root)

# Create a label
tk.Label(selection_frame, text="選擇被禁用流派:").pack(pady=10)

# Dictionary to store the variable for each class
class_vars = {
    "普攻": tk.BooleanVar(),
    "回復": tk.BooleanVar(),
    "毒": tk.BooleanVar(),
    "冰": tk.BooleanVar(),
    "閃避": tk.BooleanVar(),
    "暴擊": tk.BooleanVar(),
    "生命": tk.BooleanVar(),
    "易傷": tk.BooleanVar(),
    "護盾": tk.BooleanVar(),
    "大招": tk.BooleanVar(),
    "精靈": tk.BooleanVar(),
    "怒氣": tk.BooleanVar()
}

# Create checkboxes for class selection
for cls in class_vars:
    tk.Checkbutton(selection_frame, text=cls, variable=class_vars[cls]).pack(anchor=tk.W)

# Create a button to show the champions
tk.Button(selection_frame, text="優勢英雄", command=show_champions).pack(pady=10)

# Create a reset button
tk.Button(selection_frame, text="reset", command=reset_selection).pack(pady=5)

# Back to main menu
tk.Button(selection_frame, text="返回", command=back_to_menu).pack(pady=5)

# Frame to hold champion buttons
champion_frame = tk.Frame(selection_frame)
champion_frame.pack(pady=10)

# Text area to display results
result_text = tk.Text(selection_frame, height=5, width=40)
result_text.pack(pady=10)

# Settings frame
settings_frame = tk.Frame(root)

# Settings options
tk.Button(settings_frame, text="版本更新", command=check_for_updates).pack(pady=5)
tk.Button(settings_frame, text="Light mode", command=lambda: toggle_mode("light")).pack(pady=5)
tk.Button(settings_frame, text="Dark mode", command=lambda: toggle_mode("dark")).pack(pady=5)
tk.Button(settings_frame, text="返回", command=back_to_menu).pack(pady=5)  # Back button

# Show the main menu
show_main_menu()

# Run the GUI
root.mainloop()