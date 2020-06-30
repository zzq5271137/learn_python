"""
案例: 移除文件中的病毒代码
"""

content = []

with open("08-file_demo_2.html", "r") as fp:
    is_virus = False
    for line in fp:
        if line.startswith("<script"):
            is_virus = True
        elif line.startswith("</script>"):
            is_virus = False
            continue
        if not is_virus:
            content.append(line)

# 这里是往一个新文件中写内容(为了观察区别), 如果是要删除原有文件的病毒代码, 则往原有文件中写就好
# (因为使用"w"的方式打开文件, 会删除原有文件, 然后创建一个新的文件, 相当于原有文件的内容清空了)
with open("08-file_demo_2_cleared.html", "w") as fp:
    fp.writelines(content)
