from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, HttpUrl

class TaggedUser(BaseModel):
    id: str
    username: str
    full_name: Optional[str] = None
    is_verified: Optional[bool] = None
    profile_pic_url: Optional[HttpUrl] = None

class TopComment(BaseModel):
    comment: str
    date_of_comment: datetime
    likes: int
    num_replies: int
    user_commenting: str
    replies: List[dict] = []

class Reel(BaseModel):
    url: HttpUrl
    user_posted: str
    description: Optional[str] = None
    hashtags: List[str] = []
    num_comments: int
    date_posted: datetime
    likes: int
    views: int
    video_play_count: int
    top_comments: List[TopComment] = []
    post_id: str
    thumbnail: HttpUrl
    shortcode: str
    content_id: str
    product_type: Optional[str] = None
    coauthor_producers: List[str] = []
    tagged_users: List[TaggedUser] = []
    length: float
    video_url: HttpUrl
    audio_url: Optional[HttpUrl] = None
    posts_count: int
    followers: int
    following: int

    class Config:
        arbitrary_types_allowed = True