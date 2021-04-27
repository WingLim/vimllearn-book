import os
import linecache
import json
import fileinput
import translators

current_dir = os.path.abspath(os.getcwd())
parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
artile_path = current_dir + "/vimllearn/z"

chapters = [{"name": "", "subs": []} for _ in range(11)]

def clone_repo() -> bool:
    status = os.system("git clone https://github.com/lymslive/vimllearn.git")
    return status == 0

# print(clone_repo())

chapter_dict = {
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10
}

def add_sub_chapter(key, rawname, realname, title):
    print("adding", rawname, realname)
    chapters[key]["subs"].append([rawname, realname, title])

def add_chapter_name(key, name):
    if chapters[key]["name"] == "":
        print("adding", name)
        chapters[key]["name"] = name

def read_article_info():
    files = []
    for _, _, names in os.walk(artile_path):
        for name in names:
            files.append(name)
    
    for file in files:
        path = artile_path + "/" + file
        # 读取第一行，获取章节信息
        chapter = linecache.getline(path, 1)

        chapter_title = chapter[2:]
        chapter_title = chapter_title.rstrip("\n")

        if chapter_title[1] in chapter_dict:
            lineno = 3
            # 读取第三行，获取标题信息
            title_list = linecache.getline(path, lineno).split(" ")
            while title_list[0] != "##":
                lineno += 1
                title_list = linecache.getline(path, lineno).split(" ")
            
            # 子章节
            sub_chapter = title_list[1]
            # 文章名
            title = ' '.join(title_list[2:])
            eng_file = translators.google(title)
            true_title = sub_chapter + " " + title
            true_title = true_title.rstrip("\n")
            
            key = chapter_dict[chapter_title[1]]
            add_sub_chapter(key, file, eng_file, true_title)
            add_chapter_name(key, chapter_title)
        else:
            title = chapter_title.rstrip("\n")
            eng_file = translators.google(title)
            add_sub_chapter(0, file, eng_file, title)
            add_chapter_name(0, chapter_title)

def run_and_save():
    read_article_info()
    with open("info.json", "w", encoding="utf-8") as f:
        json.dump(chapters, f, ensure_ascii=False)

def load():
    with open("info.json", "r") as f:
        chapters = json.load(f)
    

def transfer():
    with open(current_dir + "/info.json", "r", encoding="utf-8") as f:
        chapters = json.load(f)

    make_chapter_dir()
    
    for i, chapter in enumerate(chapters):
        if i == 0:
            chapter_path = parent_dir + "/content/docs/"
            weight = 0
        else:
            chapter_path = parent_dir + f"/content/docs/chapter{i}/"
            weight = i * 10
            build_chapter_index(chapter_path, i, chapter["name"])

        # aritcle 的内容为 [原文件名, 新文件名, 文章标题]
        for article in chapter["subs"]:
            weight += 1
            title = build_title(article[2], weight)
            build_appendix(article[0], article[1])
            read_path = artile_path + "/" + article[0]
            write_path = chapter_path + article[1] + ".md"
            with open(read_path, "r", encoding="utf-8") as read_obj, open(write_path, "w", encoding="utf-8") as write_obj:
                print(f"transfering {article[0]} to {article[1]}.md")
                write_obj.write(title)
                for line in read_obj:
                    write_obj.write(line)

def build_title(title: str, weight: int):
    title = title.replace("\\", "")
    res = "---\n"
    res += f"title: {title}\n"
    res += f"weight: {weight}\n"
    res += "---\n"
    return res

def make_chapter_dir():
    chapter_path = parent_dir + "/content/docs/"
    for i in range(1, 11):
        path = chapter_path + f"chapter{i}"
        if not os.path.exists(path):
            os.mkdir(path)

def build_chapter_index(path, i, title):
    with open(path + "_index.md", "w", encoding="utf-8") as f:
        f.write("---\n"
        f"title: {title}\n"
        f"weight: {10 * i}\n"
        "bookCollapseSection: true\n"
        "---")

def build_appendix(pre, cur):
    path = parent_dir + "/content/docs/Appendix.md"
    with open(path, "a", encoding="utf-8") as f:
        text = f"|{cur}.md|[{pre}](https://github.com/lymslive/vimllearn/tree/master/z/{pre})|\n"
        f.write(text)

run_and_save()
transfer()