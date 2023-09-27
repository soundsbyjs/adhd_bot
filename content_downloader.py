# half of this file is notes, links and stuff
# half is going to be misc methods for getting content
# do not upload this to github!

import argparse
from pytube import YouTube

def download_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4') \
                       .order_by('resolution') \
                       .desc() \
                       .first()
    stream.download(output_path=output_path)
    print("Download is completed successfully.")

def main():
    parser = argparse.ArgumentParser(description="Download a YouTube video with specified URL.")
    parser.add_argument("url", type=str, help="YouTube video URL")
    parser.add_argument("-o", "--output", type=str, default="./", help="Output directory (default: current directory)")

    args = parser.parse_args()
    download_video(args.url, args.output)

if __name__ == "__main__":
    main()

