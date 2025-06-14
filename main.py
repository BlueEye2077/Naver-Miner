import requests
from bs4 import BeautifulSoup
from concurrent.futures import as_completed, ThreadPoolExecutor
from tqdm import tqdm
import os
from termcolor import colored
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.style import Style
from rich import box


def show_banner():
    console = Console()
    banner_text = Text("""
███╗   ██╗ █████╗ ██╗   ██╗███████╗██████╗     ███╗   ███╗██╗███╗   ██╗███████╗██████╗       ／＞　 フ 
████╗  ██║██╔══██╗██║   ██║██╔════╝██╔══██╗    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗     | 　_　_| 
██╔██╗ ██║███████║██║   ██║█████╗  ██████╔╝    ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝   ／` ミ＿xノ
██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗    ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗  /　　　　 |
██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║ /　 ヽ　　 ﾉ
╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝│　　|　|　|
                                                                                    ／￣|　　 |　|
                                                                                    (￣ヽ＿_ヽ_)__)
                                                                                    ＼二)
""", style=Style(color="green", bold=True))


    panel = Panel(
        banner_text,
        border_style="white",
        box=box.DOUBLE,
        expand=False,
        padding=(0, 1),
    )

    console.print(panel)
    console.print()

# ------------------------------------------------------------------------------------------------------

def get_all_images(chapter_link):

    requested_link= requests.get(chapter_link,
                        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"})

    the_soup=BeautifulSoup(requested_link.content, "lxml")

    all_images=the_soup.find("div",{"id":"sectionContWide"}).find_all("img")

    return all_images

# ------------------------------------------------------------------------------------------------------

def mk_folder(chapter_link):
    chapter_path="chapters"
    mother_folder="Downloaded Manhua"
    try:
        manhua= chapter_link[chapter_link.find("titleId=")+len("titleId="):chapter_link.index("&")]
        chapter_number=chapter_link[chapter_link.find("no=")+len("no="):chapter_link.index("&w")]


        os.mkdir(mother_folder) if not os.path.exists(mother_folder) else 0
        os.mkdir(os.path.join(mother_folder,manhua)) if not os.path.exists(os.path.join(mother_folder,manhua)) else 0
        os.mkdir(os.path.join(mother_folder,manhua,chapter_number)) if not os.path.exists(os.path.join(mother_folder,manhua,chapter_number)) else 0

        chapter_path= os.path.join(mother_folder,manhua,chapter_number)

        return chapter_path
    
    except Exception as e:
        print("Error Happend Making The Folder")
        return chapter_path

# ------------------------------------------------------------------------------------------------------

def get_all_images_links(all_images : list):
    all_src_images=[]
    for image in all_images:
        image=image.get("src").strip()
        all_src_images.append(image)

    return all_src_images

# ------------------------------------------------------------------------------------------------------

def download_image(url,saving_name):
    try:
        requested_url=requests.get(url,
                                headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"})
        folder_path=os.path.join(chapter_path,str(saving_name))
        with open(f"{folder_path}.jpg",mode="wb") as my_image:
            my_image.write(requested_url.content)

        return f"Image {saving_name} Is Downloaded"
    
    except Exception as e:
        return "Error Happend"
    
# ------------------------------------------------------------------------------------------------------

def download_all_images_concurrently(urls):
    try:
        with ThreadPoolExecutor(max_workers=10) as executor:
            features=[executor.submit(download_image,url,number) for url, number in zip(urls,range(len(urls)))]
            for feature in tqdm(as_completed(features), total=len(features), desc="Downloading"):
                result= feature.result()

        print(colored("The Chapter Is Downloaded Successfully.",color="light_green"))
        print(colored("You Can Find The Chapter In The Sub Folder Called 'Downloaded Manhua'",color="yellow"))
        input("Press Any Button To Leave...")
    except Exception as e:
        print("Error Happend While Downloding")

# ------------------------------------------------------------------------------------------------------

if __name__ == "__main__" :
    try:
        show_banner()
    except Exception :
        pass
    
    print("Please Enter The Link For The Chapter:")
    try:
        chapter_link_input=input("=>").strip()
        chapter_path=mk_folder(chapter_link_input)
        download_all_images_concurrently(get_all_images_links(get_all_images(chapter_link_input)))
    except Exception as e:
        print("Error Happened While Downloading The Chapter")




