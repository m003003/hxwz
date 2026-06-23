import os

BASE_DIRS = ['hxwz', 'zk']

def fix_file_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        stripped = line.strip()
        # 如果这一行本身就是空行，或者已经是 Markdown 标题/列表，就保持原样
        if not stripped or stripped.startswith('#') or stripped.startswith('*') or stripped.startswith('|'):
            new_lines.append(line)
        else:
            # 如果是普通文本行，确保它后面有一个空行
            new_lines.append(line)
            if not line.endswith('\n\n'):
                new_lines.append('\n')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# 递归遍历并修复
for base in BASE_DIRS:
    if os.path.exists(base):
        print(f"正在修复 {base} 目录下的段落格式...")
        for root, dirs, files in os.walk(base):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    fix_file_paragraphs(file_path)

print("段落格式全部修复完毕！")
