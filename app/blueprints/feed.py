"""
    Views for feed.
"""


from flask import Blueprint, abort, jsonify
from helpers import JSONSerialazable

from models import ResponseTemplate, FeedResponse, PostDB, FeedItemDB

feed = Blueprint('feed', __name__, url_prefix='/feed')

@feed.route('/posts', methods=['GET'])
def posts():
    feed = FeedItemDB.query_all()
    widgets = [item.to_json() for item in feed]

    feed_resp = FeedResponse('base', widgets=widgets).to_json()
    
    return jsonify(ResponseTemplate(True, payload=feed_resp).to_json()), 200

@feed.route('/post/<id>', methods=['GET'])
def post(id):
    posts = [post.to_json() for post in PostDB.query_all() if post.id == int(id)]
    if len(posts) == 1:
        return jsonify(ResponseTemplate(True, payload=posts).to_json()), 200
    elif not len(posts):
        return f'Post with id({id}) not found', 404
    else:
        return 'unexpected error', 500
