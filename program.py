import requests
from bs4 import BeautifulSoup
import pickle
import json

# get informations and write project codes in "project_codes.txt".
def write_projects_code(informations):
    codes = [info['code'] for info in informations]

    with open("projects_code.bin", 'wb') as f:
        pickle.dump(codes, f)

# read project codes as a list from "project_codes.txt".
def read_projects_code():
    codes = []
    try:
        with open("projects_code.bin", 'rb') as f:
            codes = pickle.load(f)
    except FileNotFoundError:
        pass
    return codes

# remove dublicate projects and return only new projects.
def remove_dublicate_projects(informations):
    new_codes = [info['code'] for info in informations]
    old_codes = read_projects_code()
    dublicates = []

    tmp = informations.copy()

    for c in new_codes:
        if c in old_codes:
            dublicates.append(c)

    for info in tmp:
        if info['code'] in dublicates:
            informations.remove(info)

    return informations

# write project informations in a json file.
def write_project_informations(informations):
    informations += read_project_informations()
    with open("projects_informations.json", 'w', encoding="utf-8") as f:
        json.dump(informations, f, ensure_ascii=False, indent=4)

# read project informations from a json file.
def read_project_informations():
    try:
        with open("projects_informations.json", 'r', encoding="utf-8") as f:
            informations = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
            informations = []
    return informations

# generate a code for projects from time, user_name, type and project_name
def gen_project_code(time, user_name, event_type, project_name):
    return f"{project_name}--{time}--{user_name}--{event_type}"

# get informations from typeiran.com and return a list contain project informations
def get_informations():
    page = requests.get("http://typeiran.com/").content
    soup = BeautifulSoup(page, 'lxml')
    events = soup.select("#cynic-projects > div.project-showcase > div > div > div > div > div > table > tbody > tr")

    informations = []

    for e in events:
        time = e.select("p.timeago")[0].attrs["title"]
        user_name = e.select("a.mr-2")[0].string
        user_id = e.select("a.mr-2")[0].attrs["href"]
        event_type = e.select("div.label")[0].string
        text = e.select("td span")[0].text
        project_name = e.select("td span a")[0].text
        project_url = e.select("td span a")[0].attrs['href']
        informations.append({
            'code': gen_project_code(time, user_name, event_type, project_name),
            'project_name': project_name,
            'project_url': project_url,
            'time': time,
            'user_name': user_name,
            'user_id': user_id,
            'type': event_type,
            'text': text
        })

    return informations

