import youtube_dl
import os
import argparse

YDL_OPT = {
    'format':'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }]
}


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--watch', type=str, help='url of video')
    parser.add_argument('--url', type=str, help='full url of video')
    parser.add_argument('--path', type=str, help='path to download')
    args = parser.parse_args()
    if args.watch is None and args.url is None:
        raise ValueError('Must have one argument')
    elif args.watch is not None:
        path = "https://www.youtube.com/watch?v=" + args.watch
    elif args.url is not None:
        path = args.url
    else:
        raise ValueError('Must have only one agrument')
    if args.path is None:
        output = './'
    else:
        output = agrs.path

    if not os.path.exists(output):
        os.mkdir(output)

    YDL_OPT['outtmpl'] = output + '%(title)s.%(ext)s'

    with youtube_dl.YoutubeDL(YDL_OPT) as ydl:
        ydl.download([path])

