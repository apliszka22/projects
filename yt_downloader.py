from pytube import YouTube
import sys

DOWNLOAD_DESTINATION = '/Users/adam/Dev/YouTube'  # insert you download path here
MB = 1048576


def progress_func(stream, chunk, bytes_remaining):
    curr = stream.filesize - bytes_remaining
    curr_size_mb = curr / MB
    file_size = stream.filesize / MB
    done = int(50 * curr / stream.filesize)
    sys.stdout.write(
        f"\r[{'=' * done}{' ' * (50 - done)}] {curr_size_mb:.2f} of {file_size:.2f} MB remaining {bytes_remaining / MB:.2f} MB")
    sys.stdout.flush()


def download(url):
    youtube_object = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=progress_func)
    print(f'Downloading {youtube_object.title}')
    youtube_object.streams.get_highest_resolution().download(output_path=DOWNLOAD_DESTINATION)
    print(f'\nDownload {youtube_object.title} completed successfully')


link = input("Enter the YouTube video URL: ")
download(link)
