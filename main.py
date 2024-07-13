import requests
import os
from dotenv import load_dotenv
import time

def find_image_link(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        for ln in f.readlines():
            if(ln.find('"SkinUrl"') > 0):
                for x in ln.split('"'):
                    if x.find("png") > 0 or x.find("jpeg") > 0 or x.find("jpg") > 0:
                        return x
        return ""

def upload_image_to_imgbb(api_key, image_url):
    data = {
        "key": api_key,
        "image": image_url,
    } 
    response = requests.post("https://api.imgbb.com/1/upload", data=data)
    result = []
    try:
        result = response.json()
    except:
        result = {"error": {"message": "Bad Reques, run again Code."}}
    return result

def change_image_link_in_file(file_path, old_image_link, new_image_link):
    with open(file_path, "r+", encoding="utf-8") as f:
        content = f.read()
        content = content.replace(old_image_link, new_image_link)
        f.seek(0)
        f.truncate()
        f.write(content)
    return
    
def change_link(path: str) -> int:
    old_link = find_image_link(file_path=path)

    if old_link.find("ibb") > 0:
        return 200
    
    if old_link == "":
        return ["Link not found", path, ""]

    time.sleep(3)
    data = upload_image_to_imgbb(api_key=os.getenv("API_KEY"), image_url=old_link)
    if "error" in data:
        return [data["error"]["message"], path, old_link]

    change_image_link_in_file(file_path=path, old_image_link=old_link, new_image_link=data["data"]["image"]["url"])
    return 200

def get_all_path_to_files(start_path: str = "./clones") -> list[str]:
    result = []
    for root, _, files in os.walk(start_path):
        result.append([ (root + "/" + file).replace("\\","/") for file in files if file.find("json") > 0])
    return result

def flatten_list(lst: list[list[str] | str]) -> list[str]:
    result = []
    for x in lst:
        if isinstance(x, str):
            result.append(x)
        else: 
            result.extend(flatten_list(x))
    return result


def change_something(file_path, to_change, new_value):
    with open(file_path, "r+", encoding="utf-8") as f:
        content = f.read()
        if content.find(to_change) > 0:
            content = content.replace(to_change, new_value)
        else:
            return 0 
        f.seek(0)
        f.truncate()
        f.write(content)
    return 1

if __name__ == '__main__':

    load_dotenv()
    paths_files = flatten_list(lst = get_all_path_to_files(start_path="./clones"))

    success = 0
    for path in paths_files:
        result = change_link(path=path)
        if result == 200:
            success += 1
        else:
            print("Critical error:", result[0], result [1], result[2])

    print(f"Successfully changed {success} of {len(paths_files)} links.")

    to_change = '' #example '"ReturnToStart": 1b,'
    new_value = '' #example '"ReturnToStart": 0b,'

    if(to_change != ""):
        change_success = 0 
        for path in paths_files:
            change_success += change_something(file_path=path, to_change=to_change, new_value=new_value)

        print(f"Successfully changed value in {change_success} of {len(paths_files)}.")