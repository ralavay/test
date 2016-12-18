#!/usr/bin/env python

"""
Requirements
    - Read a post by id and display the title and body on separate lines.
    - Create a post where the title and body are command line arguments
    - Update the title and body of a post by post id

API Document
    https://jsonplaceholder.typicode.com/

Usage:
    Get post content
        ./script.py get <post_id>
    Create post
        ./script.py create --title="long long title" --body="long long body"
    UPdate post
        ./script.py update <post_id> --title="long long title" --body="long long body" 
"""

import argparse
import requests


API = "http://jsonplaceholder.typicode.com/posts"


def check_post_id(post_id):
    if post_id is None:
        return False
    try:
        post_id = int(post_id)
        return post_id
    except ValueError:
        return False


def get_post(args):
    "Get post title and body by id of the post"
    post_id = args.post_id
    if not check_post_id(post_id):
        print "Please enter a number"
        return 1
    
    resp = requests.get("{}/{}".format(API, post_id))
    
    if resp.status_code == 200:
        print resp.json()['title']
        print "\n"
        print resp.json()['body']
    elif resp.status_code == 404:
        print "Post id {} was not found".format(post_id)
    else:
        print "Something went wrong"


def create_post(args):
    "Create post with title & body"
    post_content = {
        'title': args.title,
        'body': args.body
    }
    resp = requests.post(API, data=post_content)
    if resp.status_code == 201:
        print "Post is created"
    else:
        print "Something went wrong"


def update_post(args):
    "Update an existing post by post id"
    post_id = args.post_id
    post_content = {
        'title': args.title,
        'body': args.body
    }
    if not check_post_id(post_id):
        print "Please enter a number"
        return 1
    
    resp = requests.put("{}/{}".format(API, post_id), post_content)
    
    if resp.status_code == 200:
        print "Post id {} was updated".format(post_id)
    elif resp.status_code == 404:
        print "Post id {} was not found".format(post_id)
    else:
        print "Something went wrong"
    

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    get_post_parser = subparsers.add_parser('get')
    get_post_parser.add_argument('post_id')
    get_post_parser.set_defaults(func=get_post)

    create_post_parser = subparsers.add_parser('create')
    create_post_parser.add_argument('--title', required=True)
    create_post_parser.add_argument('--body', required=True)
    create_post_parser.set_defaults(func=create_post)

    update_post_parser = subparsers.add_parser('update')
    update_post_parser.add_argument('post_id')
    update_post_parser.add_argument('--title', required=True)
    update_post_parser.add_argument('--body', required=True)
    update_post_parser.set_defaults(func=update_post)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
  	main()
