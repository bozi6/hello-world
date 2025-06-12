"""Youtube Scraper."""
#  main.py Copyright (C) 2024  Konta Boáz
#      This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
#      This is free software, and you are welcome to redistribute it
#      under certain conditions; type `show c' for details.
#   Last Modified: 2024. 12. 04. 16:02

import scrapetube

# Konstansok
PLAYLIST_ID = "PLt_n2q5yoRsTKKxvpY-xzreOGO80cvBjz"
OUTPUT_FILE = "videos.txt"
UNKNOWN_TITLE = "Ismeretlen cím"
SEPARATOR_LENGTH = 80
FILE_SEPARATOR_LENGTH = 100


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

    # Rendezés cím szerint
    video_list.sort(key=lambda x: x['title'].lower())
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
    """Videólista fájlba mentése."""
    print('Azért kiírom fájlba is, hogy meglegyen.')
    with open(filename, 'w', encoding='utf-8') as f:
        for video_data in video_list:
            f.write(f"{video_data['title']}\t")
            f.write(f"URL: {video_data['url']}\n")
            f.write("-" * FILE_SEPARATOR_LENGTH + "\n")


def main():
    """Fő program logika."""
    try:
        video_list = fetch_playlist_videos(PLAYLIST_ID)
        # print_video_list(video_list, PLAYLIST_ID)
        print(f"\nÖsszesen {len(video_list)} videó található a lejátszási listában.")
        save_to_file(video_list, OUTPUT_FILE)

    except Exception as e:
        print(f"Hiba történt a lejátszási lista lekérdezése során: {e}")


if __name__ == "__main__":
    main()
