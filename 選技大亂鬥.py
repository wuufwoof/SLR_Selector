import tkinter as tk

class Champion:
    def __init__(self, name, classes):
        self.name = name
        self.classes = classes

# Define the champions with their respective classes
champions = [
    Champion("刀鋒偤長", ["普攻", "暴擊"]),  # Blade Master: Basic Attack, Critical Hit
    Champion("白虎射手", ["普攻", "回復"]),  # White Tiger Archer: Basic Attack, Heal
    Champion("毒龍騎士", ["普攻", "毒"]),    # Poison Dragon Knight: Basic Attack, Poison
    Champion("冰雪魔靈", ["普攻", "回復", "冰", "易傷", "護盾"]),  # Ice Spirit: Basic Attack, Heal, Ice, Vulnerable, Shield
    Champion("隱匿之刃", ["閃避", "回復"]),  # Shadow Blade: Dodge, Heal
    Champion("惡魔之影", ["閃避", "暴擊", "回復", "生命"]),  # Demon Shadow: Dodge, Critical Hit, Heal, Life
    Champion("魅影刺客", ["閃避", "毒"]),    # Phantom Assassin: Dodge, Poison
    Champion("破魔者", ["閃避", "回復"]),    # Demon Breaker: Dodge, Heal
    Champion("森林遊俠", ["閃避", "回復", "大招"]),  # Forest Ranger: Dodge, Heal, Ultimate
    Champion("狂暴斧王", ["暴擊", "回復", "大招"]),  # Berserk Axe King: Critical Hit, Heal, Ultimate
    Champion("極寒掌控者", ["暴擊", "冰", "大招"]),  # Extreme Cold Controller: Critical Hit, Freeze, Ultimate
    Champion("雙頭魔法師", ["暴擊", "大招"]),  # Two-headed Mage: Critical Hit, Ultimate
    Champion("覓血蛛王", ["暴擊", "毒"]),    # Blood Seeking Spider King: Critical Hit, Poison
    Champion("雷神", ["生命", "回復", "大招", "毒"]),  # Thunder God: Life, Heal, Ultimate, Poison
    Champion("深海巨人", ["生命", "回復", "毒", "冰"]),  # Deep Sea Giant: Life, Heal, Poison, Ice
    Champion("熊貓武士", ["回復", "毒", "冰"]),  # Panda Warrior: Heal, Poison, Ice
    Champion("精靈牧師", ["精靈", "回復"]),  # Elf Priest: Elf, Heal
    Champion("神秘法師", ["大招", "回復", "生命", "精靈"]),  # Mysterious Mage: Ultimate, Heal, Life, Elf
    Champion("劇毒巫師", ["毒", "回復", "精靈", "冰"]),  # Venomous Wizard: Poison, Heal, Elf, Ice
    Champion("瘟疫術士", ["毒", "回復"]),    # Plague Sorcerer: Poison, Heal
    Champion("皇家騎士", ["護盾", "毒"]),    # Royal Knight: Shield, Poison
    Champion("部落勇士", ["護盾", "毒"]),    # Tribal Warrior: Shield, Poison
    Champion("混亂使徒", ["易傷"]),        # Chaos Apostle: Vulnerable
    Champion("星界法師", ["易傷", "大招"]),  # Astral Mage: Vulnerable, Ultimate
    Champion("娜迦女王", ["冰", "易傷"]),    # Naga Queen: Ice, Vulnerable
    Champion("叢林先知", ["精靈"]),        # Jungle Prophet: Elf
    Champion("混亂魔王", ["精靈", "易傷"]),  # Chaos Apostle: Elf, Vulnerable
    Champion("樹精守衛", ["精靈", "護盾", "大招"]),  # Tree Guardian: Elf, Shield, Ultimate
    Champion("辣椒射手", ["怒氣", "易傷", "大招"]),  # Chilli Shooter: Rage, Vulnerable, Ultimate
    Champion("狂怒法師", ["怒氣", "暴擊"])   # Fury Mage: Rage, Critical Hit
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
    # Clear all checkboxes
    for var in class_vars.values():
        var.set(False)
    
    # Clear the results and champion buttons
    result_text.delete(1.0, tk.END)
    for widget in champion_frame.winfo_children():
        widget.destroy()

# Set up the GUI window
root = tk.Tk()
root.title("英雄选择器")

# Create a label
tk.Label(root, text="選擇被禁用流派:").pack(pady=10)

# Dictionary to store the variable for each class
class_vars = {
    "普攻": tk.BooleanVar(),   # Basic Attack
    "回復": tk.BooleanVar(),   # Heal
    "毒": tk.BooleanVar(),      # Poison
    "冰": tk.BooleanVar(),      # Ice
    "閃避": tk.BooleanVar(),    # Dodge
    "暴擊": tk.BooleanVar(),    # Critical Hit
    "生命": tk.BooleanVar(),    # Life
    "易傷": tk.BooleanVar(),    # Vulnerable
    "護盾": tk.BooleanVar(),    # Shield
    "大招": tk.BooleanVar(),    # Ultimate
    "精靈": tk.BooleanVar(),    # Elf
    "怒氣": tk.BooleanVar()     # Rage
}

# Create checkboxes for class selection
for cls in class_vars:
    tk.Checkbutton(root, text=cls, variable=class_vars[cls]).pack(anchor=tk.W)

# Create a button to show the champions
tk.Button(root, text="優勢英雄", command=show_champions).pack(pady=10)

# Create a reset button
tk.Button(root, text="reset", command=reset_selection).pack(pady=5)

# Frame to hold champion buttons
champion_frame = tk.Frame(root)
champion_frame.pack(pady=10)

# Text area to display results
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=10)

# Run the GUI
root.mainloop()