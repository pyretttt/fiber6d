"""
    Launch command that is used before launch.
"""

import json
import typing as t
from pathlib import Path

from models import FeedItemDB, PostDB


class TestCommand:
    """
        Pre-launch command for test configuration.
    """

    def __init__(self, test_data_path: str = 'data/test_data.json'):
        self.test_data_path = test_data_path

    def __call__(self, *args, **kwargs):
        if len(FeedItemDB.query_all()) == 0 and len(PostDB.query_all()) == 0:
            path = Path(__file__).resolve().parent.parent.parent / self.test_data_path
            with open(path) as file:
                data = json.load(file)
        
            try:
                self.fill_db(data)
            except:
                print('Unexpected error occurred, test Data not included')
        
    def fill_db(self, test_data: t.Dict[str, t.Any]):
        feed = test_data['feed']
        posts = test_data['posts']

        for item in feed:
            FeedItemDB(
                id=item['id'],
                post_id=item['post_id'],
                title=item['title'],
                subtitle=item['subtitle'],
                preview=item['preview']
            ).add()

        for post in posts:
            PostDB(
                id=post['id'],
                payload=json.dumps(post['widgets']).encode('utf-8')
            ).add()
        
if __name__ == '__main__':
    command = TestCommand('data/test_data.json')
    command()
    