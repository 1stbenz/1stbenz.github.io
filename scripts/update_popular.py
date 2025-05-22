import csv
import re
import os
import glob
import json
import sys

def update_popular(csv_path=None, limit=10):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    posts_dir = os.path.join(base_dir, "_posts")
    data_dir = os.path.join(base_dir, "_data")
    os.makedirs(data_dir, exist_ok=True)
    out_json = os.path.join(data_dir, "popular_posts.json")

    if not csv_path:
        default_downloads = os.path.expanduser(r"~\Downloads\報表數據匯報.csv")
        if os.path.exists(default_downloads):
            csv_path = default_downloads
        else:
            print("錯誤：找不到 CSV 檔案，請指定路徑，例如：python update_popular.py <csv路徑>")
            return

    print(f"讀取 CSV 報表: {csv_path}")

    # 1. 索引所有現有文章 (按檔案名稱與標題)
    # 我們以 filename 為核心關聯跨語系文章
    file_to_posts = {}
    title_to_file = {}

    lang_folders = [
        ("zh-Hant", "zh"),
        ("en", "en"),
        ("ja", "ja"),
        ("de", "de"),
        ("es", "es")
    ]

    for lang_code, folder in lang_folders:
        folder_path = os.path.join(posts_dir, folder)
        for p in glob.glob(folder_path + "/*.md"):
            fname = os.path.basename(p)
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            fm_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if not fm_match:
                continue

            fm = fm_match.group(1)
            title_m = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.M)
            image_m = re.search(r'^image:\s*["\']?(.*?)["\']?\s*$', fm, re.M)

            title = title_m.group(1).strip() if title_m else ""
            if (title.startswith('"') and title.endswith('"')) or (title.startswith("'") and title.endswith("'")):
                title = title[1:-1].strip()

            image = image_m.group(1).strip() if image_m else ""

            m = re.match(r"^(\d{4})-\d{2}-\d{2}-(.*?)\.md$", fname)
            if m:
                year, slug = m.group(1), m.group(2)
                if folder == "zh":
                    url = f"/{year}/{slug}.html"
                else:
                    url = f"/{folder}/{year}/{slug}.html"

                if fname not in file_to_posts:
                    file_to_posts[fname] = {}

                file_to_posts[fname][lang_code] = {
                    "title": title,
                    "url": url,
                    "image": image,
                    "fname": fname
                }
                title_to_file[title] = fname

    # 2. 解析 GA4 匯出的 CSV
    with open(csv_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    start_date, end_date = "", ""
    for line in lines:
        if "開始日期：" in line:
            start_date = line.split("：")[1].strip()
        if "結束日期：" in line:
            end_date = line.split("：")[1].strip()

    data_lines = []
    found = False
    for line in lines:
        if "網頁標題與畫面類別" in line:
            found = True
            data_lines.append(line)
        elif found:
            if line.startswith("#"):
                break
            data_lines.append(line)

    reader = csv.DictReader(data_lines)
    top_fnames = []
    seen_fnames = set()

    for row in reader:
        raw_title = row.get("網頁標題與畫面類別", "").strip()
        views_str = row.get("瀏覽", "0").replace(",", "")
        try:
            views = int(views_str)
        except ValueError:
            views = 0

        clean_title = re.sub(r"\s*\|\s*(中年阿賓の玩具|1stBenz's Toys|1stBenz' Spielzeuge|Juguetes de 1stBenz|中年阿賓のオモチャ).*$", "", raw_title).strip()

        if not clean_title or clean_title in ["中年阿賓の玩具", "1stBenz's Toys", "1stBenz' Spielzeuge", "Juguetes de 1stBenz", "中年阿賓のオモチャ", "首頁", "Home"]:
            continue

        matched_fname = None
        if clean_title in title_to_file:
            matched_fname = title_to_file[clean_title]
        else:
            for t, fn in title_to_file.items():
                if clean_title == t or clean_title in t or t in clean_title:
                    matched_fname = fn
                    break

        if matched_fname and matched_fname not in seen_fnames:
            seen_fnames.add(matched_fname)
            top_fnames.append((matched_fname, views))
            if len(top_fnames) >= limit:
                break

    # 3. 整理各語系排行榜
    update_str_zh = f"{end_date[:4]}.{end_date[4:6]} 更新" if end_date and len(end_date) == 8 else "本月更新"
    update_str_en = f"{end_date[:4]}.{end_date[4:6]} Updated" if end_date and len(end_date) == 8 else "Updated"
    update_str_de = f"{end_date[:4]}.{end_date[4:6]} Aktualisiert" if end_date and len(end_date) == 8 else "Aktualisiert"
    update_str_es = f"{end_date[:4]}.{end_date[4:6]} Actualizado" if end_date and len(end_date) == 8 else "Actualizado"

    output_data = {
        "update_date": update_str_zh,
        "update_date_en": update_str_en,
        "update_date_de": update_str_de,
        "update_date_es": update_str_es,
        "date_range": f"{start_date} - {end_date}" if start_date else "",
    }

    for lang_code, folder in lang_folders:
        lang_list = []
        for fname, views in top_fnames:
            post_info = file_to_posts.get(fname, {}).get(lang_code)
            # 若該語系剛好沒有翻譯，則回退到中文資訊
            if not post_info:
                post_info = file_to_posts.get(fname, {}).get("zh-Hant")

            if post_info:
                # 確保縮圖存在，若該語系沒寫 image，取中文文章的 image
                img = post_info.get("image")
                if not img:
                    img = file_to_posts.get(fname, {}).get("zh-Hant", {}).get("image", "")

                lang_list.append({
                    "title": post_info["title"],
                    "url": post_info["url"],
                    "image": img,
                    "views": views
                })
        output_data[lang_code] = lang_list

    # 兼容舊版 Liquid 語法
    output_data["posts"] = output_data["zh-Hant"]

    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"成功更新全語系熱門文章排行榜！已儲存至：{out_json}")
    print(f"各語系篇數：zh={len(output_data['zh-Hant'])}, en={len(output_data['en'])}, ja={len(output_data['ja'])}, de={len(output_data['de'])}, es={len(output_data['es'])}")

if __name__ == "__main__":
    target_csv = sys.argv[1] if len(sys.argv) > 1 else None
    update_popular(target_csv)
