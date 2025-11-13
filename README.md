# Instagram Reels Scraper

> Instagram Reels Scraper helps you collect detailed, structured data from public Instagram Reels URLs. It captures reel metadata, engagement metrics, user statistics, and media assets so you can analyze performance, monitor campaigns, and power your own analytics dashboards.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Instagram Reels Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

Instagram Reels Scraper is a specialized tool that takes one or more valid Instagram Reel links and turns them into rich, machine-readable data. It removes the manual effort of opening each reel, checking views, likes, comments, and user stats, and instead gives you a clean JSON output you can plug into your own tools.

This project is ideal for:

- Social media analysts tracking reel performance over time
- Marketing teams and agencies running influencer or UGC campaigns
- Product teams building internal dashboards for Instagram monitoring
- Researchers studying short-form video performance and engagement

### Reels Intelligence & Engagement Insights

- Extracts core reel information, including URL, caption, hashtags, and posting time.
- Captures full engagement metrics such as likes, views, comments, and play count.
- Gathers detailed user statistics: followers, following, and total posts.
- Includes top comments with timestamps, likes, replies, and commenting user handles.
- Retrieves media URLs (video, thumbnail, audio) and content type for downstream processing.

## Features

| Feature | Description |
|--------|-------------|
| Comprehensive reel metadata | Collects URLs, captions, hashtags, posting dates, and identifiers for each reel. |
| Engagement analytics | Captures likes, views, comment counts, and video play count for deeper performance analysis. |
| Top comments harvesting | Retrieves top comments with user handles, timestamps, likes, and reply threads. |
| User statistics snapshot | Includes follower counts, following counts, and total posts of the reel owner. |
| Media asset collection | Provides direct links to thumbnails, video files, and associated audio pages. |
| Co-author & tagging details | Lists co-author usernames and tagged user details, including verification and profile image. |
| Content specification | Exposes product type, reel length (duration), and content identifiers for precise tracking. |
| Clean JSON output | Returns structured JSON suitable for data pipelines, dashboards, and machine learning workflows. |
| Flexible integration | Designed to be integrated into scripts, automation pipelines, or backend services. |
| Use-case ready design | Optimized for analytics, marketing research, influencer tracking, and content strategy tasks. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|-----------|------------------|
| `url` | Direct URL of the Instagram reel. |
| `user_posted` | Username of the account that published the reel. |
| `description` | Full caption/description text associated with the reel. |
| `hashtags` | Array of hashtags parsed from the reel caption. |
| `num_comments` | Total number of comments on the reel. |
| `date_posted` | ISO timestamp of when the reel was posted. |
| `likes` | Total number of likes the reel has received. |
| `views` | Total number of views recorded for the reel. |
| `video_play_count` | Number of times the video has been played (play count). |
| `top_comments` | Array of top comments, including comment text, user, likes, replies, and timestamps. |
| `post_id` | Unique identifier for the reel post. |
| `thumbnail` | URL of the reel’s thumbnail image. |
| `shortcode` | Instagram shortcode used to generate the reel URL. |
| `content_id` | Unique content identifier for the reel instance. |
| `product_type` | Type of media content (for example, `clips`). |
| `coauthor_producers` | List of usernames that are co-authors on the reel. |
| `tagged_users` | Array of tagged user objects, including username, full name, verification, and profile picture. |
| `length` | Duration of the reel in seconds (as a string). |
| `video_url` | Direct URL to the video file for the reel. |
| `audio_url` | URL of the audio resource used in the reel. |
| `posts_count` | Total number of posts published by the reel owner. |
| `followers` | Number of followers of the account that posted the reel. |
| `following` | Number of other accounts that the poster is following. |

---

## Example Output

    [
      {
        "url": "https://www.instagram.com/p/DDb5uxNyWa9/",
        "user_posted": "gaung_merah",
        "description": "Haru biru di balik perayaan 1 juta penonton Gaung Merah SeGALAnya! Merekalah yang selalu menyalakan semangat everlasting untuk menciptakan memori yang tak lekang oleh waktu! \n\n#GaungMerah #KualitasMenyalaDariWaktukeWaktu #gaungmerahsegalanya",
        "hashtags": [
          "#GaungMerah",
          "#KualitasMenyalaDariWaktukeWaktu",
          "#gaungmerahsegalanya"
        ],
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
            "user_commenting": "ethica_shopputri"
          },
          {
            "comment": "Lamongan",
            "date_of_comment": "2024-12-21T03:50:35.000Z",
            "likes": "4",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "x_mennt"
          },
          {
            "comment": "Kota palu kpn om. ??🔥",
            "date_of_comment": "2024-12-15T08:46:16.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "uchil_djaelangkara"
          },
          {
            "comment": "MADURA YUK ..KAPAAN..😢",
            "date_of_comment": "2024-12-13T09:01:52.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "lestarilestari8879"
          },
          {
            "comment": "🔥🔥🔥 sayang g ada ke Berau 😂",
            "date_of_comment": "2024-12-13T05:06:26.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "ani.kusmanadi"
          },
          {
            "comment": "Sehat semua nya buat kluarga bang iwan fals dan kru nya",
            "date_of_comment": "2024-12-13T04:38:40.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "ridwan_fals_dksh"
          },
          {
            "comment": "Muantaaaapppp🔥🔥🔥",
            "date_of_comment": "2024-12-12T15:47:27.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "yoggie_2000"
          },
          {
            "comment": "Keren👏👏",
            "date_of_comment": "2024-12-12T15:37:03.000Z",
            "likes": "7",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "amhasagaf"
          },
          {
            "comment": "🔥🔥🔥🔥🔥🔥🔥",
            "date_of_comment": "2024-12-12T11:06:52.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "trisuangsih5"
          },
          {
            "comment": "Sehat terus crew gudang garam dan band Iwan fals semuanya pada sehat terus semoga kembali hadir lg di kota JEMBER , salam dari Oi JEMBER✌🏼🇲🇨",
            "date_of_comment": "2024-12-12T10:24:55.000Z",
            "likes": "6",
            "num_replies": 0,
            "replies": [],
            "user_commenting": "sambo_konglomrat"
          }
        ],
        "post_id": "3520661436311889597",
        "thumbnail": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-15/470032408_17976995003792378_5649157389110621603_n.jpg?stp=c0.420.1080.1080a_dst-jpg_e35_s640x640_sh0.08_tt6&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=102&_nc_ohc=X1GeQCKnvWAQ7kNvgG0Y_fP&_nc_gid=9bb6f25f41dd4f1bbf36c945bd090264&edm=AABBvjUBAAAA&ccb=7-5&oh=00_AYCS_E-pM1k3cD0udjSJ-zkeOkLLiZMCakZVEPw5MW1xAg&oe=678FB692&_nc_sid=4f4799",
        "shortcode": "DDb5uxNyWa9",
        "content_id": "3520661436311889597_53789136377",
        "product_type": "clips",
        "coauthor_producers": [
          "iwanfals"
        ],
        "tagged_users": [
          {
            "full_name": "Virgiawan Listanto",
            "id": "7559709",
            "is_verified": true,
            "profile_pic_url": "https://scontent-ber1-1.cdninstagram.com/v/t51.2885-19/375929230_549369380649571_2050279282174607290_n.jpg?stp=dst-jpg_s150x150_tt6&_nc_ht=scontent-ber1-1.cdninstagram.com&_nc_cat=107&_nc_ohc=OtpABjI5NIkQ7kNvgHNoj3j&_nc_gid=9bb6f25f41dd4f1bbf36c945bd090264&edm=AABBvjUBAAAA&ccb=7-5&oh=00_AYAL3B7Ws0qJ0lyll933-gNEr6I3G5pc7ItEGvUdCigSGQ&oe=678FD37D&_nc_sid=4f4799",
            "username": "iwanfals"
          }
        ],
        "length": "143.172",
        "video_url": "https://scontent-ber1-1.cdninstagram.com/o1/v/t16/f2/m86/AQOabMlpRPCiDUvG0mwyWO_MM6LRi9gpYLmm62CimiH-HnNXIpL1wfRom8nlrPLBRYK5qoMh7KBOFfLDiMvvS_EHTmUDKV0W8epicKk.mp4?stp=dst-mp4&efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2xpcHMuYzIuNzIwLmJhc2VsaW5lIn0&_nc_cat=104&vs=778168494475226_1774937878&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC9BRTRFQTVFOTM5QTQ4NzMzQjlEMDk1N0U5M0RCRjFBRF92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dNWklBaHgwVkZqbVl2Y0RBSXRqMmlUWGxuVTlicV9FQUFBRhUCAsgBACgAGAAbABUAACbEoa/9xZqOQBUCKAJDMywXQGHlT987ZFoYEmRhc2hfYmFzZWxpbmVfMV92MREAdf4HAA==&ccb=9-4&oh=00_AYDrdNVkUhQ-x6BWjvVvawnuxmlCKkoYfcEhepy3oR3IYQ&oe=678BDA69&_nc_sid=4f4799",
        "audio_url": "https://www.instagram.com/reels/audio/1322319278943516",
        "posts_count": 756,
        "followers": 64251,
        "following": 0
      }
    ]

---

## Directory Structure Tree

    instagram-reels-scraper (Instagram Reels Scraper)/
    ├── src/
    │   ├── main.py
    │   ├── cli.py
    │   ├── config/
    │   │   ├── settings.py
    │   │   └── settings.example.json
    │   ├── instagram_reels/
    │   │   ├── __init__.py
    │   │   ├── client.py
    │   │   ├── parser.py
    │   │   ├── models.py
    │   │   ├── validators.py
    │   │   └── rate_limiter.py
    │   ├── pipelines/
    │   │   ├── runner.py
    │   │   ├── storage.py
    │   │   └── exporters.py
    │   └── utils/
    │       ├── logging_utils.py
    │       ├── time_utils.py
    │       └── retry.py
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample_output.json
    ├── tests/
    │   ├── test_parser.py
    │   ├── test_client.py
    │   └── test_end_to_end.py
    ├── docs/
    │   └── usage-examples.md
    ├── .env.example
    ├── requirements.txt
    ├── pyproject.toml
    └── README.md

---

## Use Cases

- **Social media analysts** use it to collect reel-level engagement data, so they can benchmark performance across creators, campaigns, or time periods.
- **Agencies and brands** use it to track influencer reels, so they can verify deliverables, measure ROI, and optimize creator partnerships.
- **Market researchers** use it to analyze trends in short-form video, so they can understand which topics, sounds, and formats perform best.
- **Growth marketers** use it to monitor competitor reels, so they can reverse-engineer winning hooks, captions, and posting times.
- **Product and data teams** use it to feed dashboards and machine learning models, so they can forecast performance and recommend content strategies.

---

## FAQs

**Q1: What input does this scraper need?**
Provide one or more valid Instagram Reel URLs (public content only). You can supply them via a text file, command line arguments, or an integration that passes URLs into the pipeline.

**Q2: Does this scraper work with private or restricted accounts?**
No. It only collects data from reels that are publicly accessible. If a reel is deleted, made private, or region-restricted, the scraper will either skip it or return a structured error for that item.

**Q3: What format is the output in?**
The scraper outputs structured JSON. Each reel becomes one JSON object containing all captured fields such as metadata, engagement metrics, user statistics, and media URLs. You can easily transform this into CSV, a database table, or analytics warehouse.

**Q4: Can I integrate this with my existing analytics stack?**
Yes. The project is organized for easy integration: you can call the main scraping pipeline from your own code, or extend the `exporters` module to push results into storage targets like S3, SQL databases, or BI tools.

---

## Performance Benchmarks and Results

- **Primary Metric (Speed):** Optimized to process dozens of reels per minute on a typical broadband connection, depending on network latency and rate limits.
- **Reliability Metric (Stability):** Uses retry logic and lightweight rate limiting to maintain a high success rate when fetching reel data, even under intermittent network issues.
- **Efficiency Metric (Resource Usage):** Designed as a lightweight Python project with minimal dependencies, keeping CPU and memory usage low for batch runs or server deployments.
- **Quality Metric (Data Completeness):** Targets a comprehensive set of fields for each reel, focusing on engagement metrics, user stats, and media URLs, so downstream analysis has the context needed for accurate insights.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
