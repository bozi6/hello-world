"""Youtube Scraper."""
#  main.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 04. 16:02

import scrapetube
import unicodedata
from datetime import datetime

# Konstansok
PLAYLIST_ID = "PLt_n2q5yoRsTKKxvpY-xzreOGO80cvBjz"
OUTPUT_FILE = "videos.txt"
HTML_OUTPUT_FILE = "videos.html"
UNKNOWN_TITLE = "Ismeretlen cím"
SEPARATOR_LENGTH = 80
FILE_SEPARATOR_LENGTH = 89


def hungarian_sort_key(text):
    """Magyar karakterek szerinti rendezési kulcs."""
    # Akcentusok eltávolítása és normalizálás
    normalized = unicodedata.normalize('NFD', text.lower())
    # Csak az alapkaraktereket tartjuk meg
    ascii_text = ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
    return ascii_text


def extract_video_title(video):
    """Videó címének kinyerése a video objektumból."""
    title_runs = video.get('title', {}).get('runs', [])
    if title_runs:
        return title_runs[0].get('text', UNKNOWN_TITLE)
    return UNKNOWN_TITLE


def create_video_data(video):
    """Video adatok létrehozása strukturált formában."""
    title = extract_video_title(video)
    video_id = video['videoId']
    return {
        'title'   : title,
        'video_id': video_id,
        'url'     : f'https://www.youtube.com/watch?v={video_id}'
    }


def fetch_playlist_videos(playlist_id):
    """Lejátszási lista videóinak lekérdezése és feldolgozása."""
    videos = scrapetube.get_playlist(playlist_id)
    video_list = []

    for video in videos:
        video_data = create_video_data(video)
        video_list.append(video_data)

    # Magyar karakterek szerinti rendezés - biztonságos verzió
    video_list.sort(key=lambda x: hungarian_sort_key(x['title']))

    return video_list


def print_video_list(video_list, playlist_id):
    """Videólista konzolra történő kiírása."""
    print(f"Lista videó címek szerint: (ID: {playlist_id}):")
    print("=" * SEPARATOR_LENGTH)

    for i, video_data in enumerate(video_list, 1):
        print(f"{i}. {video_data['title']}")
        print(f"   URL: {video_data['url']}")
        print("-" * SEPARATOR_LENGTH)

    print(f"\nÖsszesen {len(video_list)} videó található a lejátszási listában.")


def save_to_file(video_list, filename):
    """Videólista fájlba mentése balra-jobbra rendezve."""
    print('Azért kiírom fájlba is, hogy meglegyen.')

    # Leghosszabb cím hosszának meghatározása a megfelelő igazításhoz
    max_title_length = max(len(video_data['title']) for video_data in video_list) if video_list else 0

    with open(filename, 'w', encoding='utf-8') as f:
        for i, video_data in enumerate(video_list, 1):
            # Sorszámozott formátum
            formatted_line = f"{i:2}; - {video_data['title']:<{max_title_length}} | {video_data['url']}\n"
            f.write(formatted_line)


def save_to_html(video_list, filename, playlist_id):
    """Videólista HTML fájlba mentése linkekkel."""
    print('HTML fájl létrehozása...')
    
    # Video lista HTML generálása
    video_items = []
    for i, video_data in enumerate(video_list, 1):
        video_html = f'''        <div class="video-item">
            <div class="video-number">{i:2}.</div>
            <div class="video-title">
                <a href="{video_data['url']}" target="_blank" title="Megnyitás új ablakban">
                    {video_data['title']}
                </a>
                <span class="youtube-icon">▶</span>
            </div>
        </div>'''
        video_items.append(video_html)
    
    # HTML sablon - egyszerű string formázással
    generation_date = datetime.now().strftime("%Y. %m. %d. %H:%M")
    total_videos = len(video_list)
    video_list_html = '\n'.join(video_items)
    
    html_content = f"""<!DOCTYPE html>
<html lang="hu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Videólista</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            line-height: 1.6;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            font-weight: 300;
        }}
        .header p {{
            margin: 10px 0 0 0;
            opacity: 0.9;
            font-size: 1.1em;
        }}
        .stats {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .video-container {{
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }}
        .video-item {{
            display: flex;
            align-items: center;
            padding: 15px 20px;
            border-bottom: 1px solid #eee;
            transition: background-color 0.3s ease;
        }}
        .video-item:hover {{
            background-color: #f8f9fa;
        }}
        .video-item:last-child {{
            border-bottom: none;
        }}
        .video-number {{
            min-width: 50px;
            font-weight: bold;
            color: #667eea;
            font-size: 1.1em;
        }}
        .video-title {{
            flex: 1;
            margin-left: 15px;
        }}
        .video-title a {{
            color: #333;
            text-decoration: none;
            font-weight: 500;
            font-size: 1.05em;
        }}
        .video-title a:hover {{
            color: #667eea;
            text-decoration: underline;
        }}
        .youtube-icon {{
            color: #ff0000;
            margin-left: 10px;
            font-size: 1.2em;
        }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            font-size: 0.9em
        }}
        .search-box {{
            margin-bottom: 20px;
            text-align: center;
        }}
        .search-box input {{
            padding: 12px 20px;
            width: 300px;
            border: 2px solid #ddd;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s ease;
        }}
        .search-box input:focus {{
            border-color: #667eea;
        }}
        @media (max-width: 768px) {{
            .video-item {{
                flex-direction: column;
                align-items: flex-start;
                padding: 12px 15px;
            }}
            .video-title {{
                margin-left: 0;
                margin-top: 8px;
                width: 100%;
            }}
            .header h1 {{
                font-size: 2em;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📺 YouTube Videólista</h1>
        <p>Generálva: {generation_date} • Playlist ID: {playlist_id}</p>
    </div>
    
    <div class="stats">
        <h3>📊 Statisztikák</h3>
        <p><strong>{total_videos}</strong> videó található a lejátszási listában</p>
    </div>
    
    <div class="search-box">
        <input type="text" id="searchInput" placeholder="🔍 Keresés a videók között..." onkeyup="searchVideos()">
    </div>
    
    <div class="video-container" id="videoContainer">
        {video_list_html}
    </div>
    
    <div class="footer">
        <p>© 2024 YouTube Scraper • Konta Boáz</p>
        <p>Ez a lista automatikusan generálódott a YouTube lejátszási listából</p>
    </div>

    <script>
        function searchVideos() {{
            const input = document.getElementById('searchInput');
            const filter = input.value.toLowerCase();
            const container = document.getElementById('videoContainer');
            const items = container.getElementsByClassName('video-item');
            
            for (let i = 0; i < items.length; i++) {{
                const title = items[i].getElementsByClassName('video-title')[0];
                if (title) {{
                    const textValue = title.textContent || title.innerText;
                    if (textValue.toLowerCase().indexOf(filter) > -1) {{
                        items[i].style.display = '';
                    }} else {{
                        items[i].style.display = 'none';
                    }}
                }}
            }}
        }}
        
        // Video link click tracking
        document.addEventListener('click', function(e) {{
            if (e.target.tagName === 'A' && e.target.href.includes('youtube.com')) {{
                console.log('Video clicked:', e.target.textContent);
            }}
        }});
    </script>
</body>
</html>"""
    
    # HTML fájl írása
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f'✅ HTML fájl sikeresen létrehozva: {filename}')


def main():
    """Fő program logika."""
    try:
        video_list = fetch_playlist_videos(PLAYLIST_ID)
        print(f"\n📊 Összesen {len(video_list)} videó található a lejátszási listában.")
        
        # Szöveges fájl mentése
        save_to_file(video_list, OUTPUT_FILE)
        print(f"✅ Szöveges lista mentve: {OUTPUT_FILE}")
        
        # HTML fájl mentése
        save_to_html(video_list, HTML_OUTPUT_FILE, PLAYLIST_ID)
        
        print(f"\n🎉 Mindkét fájl sikeresen létrehozva!")
        print(f"📄 Szöveges: {OUTPUT_FILE}")
        print(f"🌐 HTML: {HTML_OUTPUT_FILE}")

    except Exception as e:
        print(f"❌ Hiba történt a lejátszási lista lekérdezése során: {e}")


if __name__ == "__main__":
    main()