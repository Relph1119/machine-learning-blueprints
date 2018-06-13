import pandas as pd
import numpy as np
import requests
import json


myun = "a8215965"
mypw = "241abdbfe07adebaa066c589c313de8f92b476c5"

my_starred_repos = []


def get_starred_by_me():
    resp_list = []
    last_resp = ''
    first_url_to_get = 'https://api.github.com/user/starred'
    first_url_resp = requests.get(first_url_to_get, auth=(myun, mypw))
    last_resp = first_url_resp
    resp_list.append(json.loads(first_url_resp.text))

    while last_resp.links.get('next'):
        next_url_to_get = last_resp.links['next']['url']
        next_url_resp = requests.get(next_url_to_get, auth=(myun, mypw))
        last_resp = next_url_resp
        resp_list.append(json.loads(next_url_resp.text))

    for i in resp_list:
        for j in i:
            msr = j['html_url']
            my_starred_repos.append(msr)

get_starred_by_me()
#print(my_starred_repos)

my_starred_users = []
for ln in my_starred_repos:
    right_split = ln.split('.com/')[1]
    starred_usr = right_split.split('/')[0]
    my_starred_users.append(starred_usr)

print(my_starred_users)

starred_repos = {k: [] for k in set(my_starred_users)}


def get_starred_by_user(user_name):
    starred_resp_list = []
    last_resp = ''
    first_url_to_get = 'https://api.github.com/users/' + user_name + '/starred'
    first_url_resp = requests.get(first_url_to_get, auth=(myun, mypw))
    last_resp = first_url_resp
    starred_resp_list.append(json.loads(first_url_resp.text))

    while last_resp.links.get('next'):
        next_url_to_get = last_resp.links['next']['url']
        next_url_resp = requests.get(next_url_to_get, auth=(myun, mypw))
        last_resp = next_url_resp
        starred_resp_list.append(json.loads(next_url_resp.text))

    for i in starred_resp_list:
        for j in i:
            sr = j['html_url']
            starred_repos.get(user_name).append(sr)

for usr in list(set(my_starred_users)):
    print(usr)
    try:
        get_starred_by_user(usr)
    except:
        print('failed for user', usr)

repo_vocab = [item for sl in list(starred_repos.values()) for item in sl]
repo_set = list(set(repo_vocab))
#len(repo_vocab)

all_usr_vector = []
for k,v in starred_repos.items():
    usr_vector = []
    for url in repo_set:
        if url in v:
            usr_vector.extend([1])
        else:
            usr_vector.extend([0])
    all_usr_vector.append(usr_vector)

df = pd.DataFrame(all_usr_vector, columns=repo_set, index=starred_repos.keys())

my_repo_comp = []
for i in df.columns:
    if i in my_starred_repos:
        my_repo_comp.append(1)
    else:
        my_repo_comp.append(0)

mrc = pd.Series(my_repo_comp).to_frame(myun).T
mrc.columns = df.columns

fdf = pd.concat([df, mrc])


