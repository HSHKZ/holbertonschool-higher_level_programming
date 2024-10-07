#!/usr/bin/python3
'''2.processing data from the API using Python.'''

import csv
import requests

def fetch_and_print_posts():
    '''fetches all post from JSONPlaceholder'''
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(reponse.status_code))
    if reponse.status_code == 200:
        posts = reponse.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    '''fetches all post from JSONPlaceholder'''
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    if reponse.status_code == 200:
        posts = reponse.json()
        posts_list = [{"id": post["id"], "title": post["title"],
                       "body": post["body"]} for post in posts]
        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts_list:
                writer.writerow(post)
