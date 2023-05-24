import re
import requests
import time

def get_direct_download_link(mediafire_link):
    session = requests.Session()
    response = session.get(mediafire_link)
    match = re.search(r"window\.location\.href = '(.+?)'", response.text)
    if match:
        direct_download_link = match.group(1)
        return direct_download_link
    else:
        print(f"Lien de téléchargement direct non trouvé pour: {mediafire_link}")
        print(response.text)
        return "Lien de téléchargement direct non trouvé"

input_file = "liens_mediafire.txt"
output_file = "liens_telechargement_direct.txt"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        mediafire_link = line.strip()
        print(f"Traitement du lien: {mediafire_link}")
        direct_download_link = get_direct_download_link(mediafire_link)
        print(f"Lien de téléchargement direct: {direct_download_link}")
        f_out.write(direct_download_link + "\n")
        time.sleep(10)
