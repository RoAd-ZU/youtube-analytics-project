from src.channel import Channel
import json
import os
from googleapiclient.discovery import build


class Video:

    def __init__(self, video_id):
        self.video_id = video_id
        self.youtube = Channel.get_service()
        self.video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=video_id).execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/' + self.video_id
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о видео."""
        print(json.dumps(self.video, indent=2, ensure_ascii=False))

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
        self.youtube = Channel.get_service()
        self.video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=video_id).execute()
        self.title = self.video['items'][0]['snippet']['title']
        self.url = 'https://www.youtube.com/' + self.video_id
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']


"""Сделал для получения информации о видео"""
# vi = Video('AWX4JnAnjBE')
# vi.print_info()
