import json
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.youtube = Channel.get_service()
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.channel_id = channel_id
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = 'https://www.youtube.com/channel/' + channel_id
        self.subscriber_count = int(self.channel["items"][0]["statistics"]["subscriberCount"])
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.view_count = self.channel["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, jsonfile):
        data = [{'id': self.channel_id,
                 'title': self.title,
                 'description': self.description,
                 'url': self.url,
                 'subscriber_count': self.subscriber_count,
                 'video_count': self.video_count,
                 'view_count': self.view_count}]
        with open(jsonfile, 'w', ) as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def __str__(self):
        return f'{self.title} {self.url}'

    def __add__(self, other):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __sub__(self, other):
        return other.subscriber_count - self.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count


api_key: str = os.getenv('API_KEY')
"""Здесь оставил некоторые проверки для себя"""
# chan_youtube = Channel(api_key)
# chan_youtube.print_info()
