import sys
from pathlib import Path

# Ensure src/ is on sys.path so we can import the package layout.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from instagram_reels.parser import parse_reel_payload  # type: ignore  # noqa: E402
from instagram_reels.models import Reel  # type: ignore  # noqa: E402

SAMPLE_PAYLOAD = {
    "url": "https://www.instagram.com/p/DDb5uxNyWa9/",
    "user_posted": "gaung_merah",
    "description": "Haru biru di balik perayaan 1 juta penonton Gaung Merah SeGALAnya! "
    "Merekalah yang selalu menyalakan semangat everlasting untuk menciptakan memori "
    "yang tak lekang oleh waktu!\n\n#GaungMerah #KualitasMenyalaDariWaktukeWaktu #gaungmerahsegalanya",
    "hashtags": [],
    "num_comments": 50,
    "date_posted": "2024-12-11T11:15:29.000Z",
    "likes": 3120,
    "views": 42785,
    "video_play_count": 118467,
    "top_comments": [
        {
            "comment": "Alhamdulillah luar biasa ❤️❤️❤️❤️🔥🔥🔥🔥",
            "date_of_comment": "2024-12-26T02:08:07.000Z",
            "likes": "3",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "ethica_shopputri",
        }
    ],
    "post_id": "3520661436311889597",
    "thumbnail": "https://example.com/thumb.jpg",
    "shortcode": "DDb5uxNyWa9",
    "content_id": "3520661436311889597_53789136377",
    "product_type": "clips",
    "coauthor_producers": ["iwanfals"],
    "tagged_users": [
        {
            "full_name": "Virgiawan Listanto",
            "id": "7559709",
            "is_verified": True,
            "profile_pic_url": "https://example.com/profile.jpg",
            "username": "iwanfals",
        }
    ],
    "length": "143.172",
    "video_url": "https://example.com/video.mp4",
    "audio_url": "https://www.instagram.com/reels/audio/1322319278943516",
    "posts_count": 756,
    "followers": 64251,
    "following": 0,
}

def test_parse_reel_payload_basic_fields() -> None:
    reel: Reel = parse_reel_payload(SAMPLE_PAYLOAD)
    assert reel.url == SAMPLE_PAYLOAD["url"]
    assert reel.user_posted == "gaung_merah"
    assert reel.post_id == "3520661436311889597"
    assert reel.likes == 3120
    assert reel.views == 42785
    assert reel.video_play_count == 118467
    assert reel.length == float("143.172")

def test_parse_reel_payload_hashtags_extracted_when_missing() -> None:
    payload = dict(SAMPLE_PAYLOAD)
    payload["hashtags"] = []
    reel: Reel = parse_reel_payload(payload)
    assert "#GaungMerah" in reel.hashtags
    assert "#gaungmerahsegalanya" in reel.hashtags

def test_parse_reel_payload_top_comments_and_tagged_users() -> None:
    reel: Reel = parse_reel_payload(SAMPLE_PAYLOAD)
    assert len(reel.top_comments) == 1
    comment = reel.top_comments[0]
    assert comment.user_commenting == "ethica_shopputri"
    assert comment.likes == 3

    assert len(reel.tagged_users) == 1
    tagged = reel.tagged_users[0]
    assert tagged.username == "iwanfals"
    assert tagged.is_verified is True