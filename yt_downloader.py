import os
import time

import colorama
import pytube
import pytube.exceptions

LOGO = f'''{colorama.Fore.RED}
 ▓█████▄  ▒█████   █     █░ ███▄    █   ██▓    ▒█████   ▄▄▄     ▓█████▄  ▓█████ ██▀███      
 ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░ ██ ▀█   █  ▓██▒   ▒██▒  ██▒▒████▄   ▒██▀ ██▌ ▓█   ▀▓██ ▒ ██▒    
 ░██   █▌▒██░  ██▒▒█░ █ ░█ ▓██  ▀█ ██▒ ▒██░   ▒██░  ██▒▒██  ▀█▄ ░██   █▌ ▒███  ▓██ ░▄█ ▒    
▒░▓█▄   ▌▒██   ██░░█░ █ ░█ ▓██▒  ▐▌██▒ ▒██░   ▒██   ██░░██▄▄▄▄██░▓█▄   ▌ ▒▓█  ▄▒██▀▀█▄      
░░▒████▓ ░ ████▓▒░░░██▒██▓ ▒██░   ▓██░▒░██████░ ████▓▒░▒▓█   ▓██░▒████▓ ▒░▒████░██▓ ▒██▒    
░ ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▒░   ▒ ▒ ░░ ▒░▓  ░ ▒░▒░▒░ ░▒▒   ▓▒█ ▒▒▓  ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░    
  ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  ░ ░░   ░ ▒░░░ ░ ▒    ░ ▒ ▒░ ░ ░   ▒▒  ░ ▒  ▒ ░ ░ ░    ░▒ ░ ▒     
  ░ ░  ░ ░ ░ ░ ▒    ░   ░     ░   ░ ░    ░ ░  ░ ░ ░ ▒    ░   ▒   ░ ░  ░     ░    ░░   ░     
    ░        ░ ░      ░             ░ ░    ░      ░ ░        ░     ░    ░   ░     ░         
                            CTRL + C to close the program.
                                
                                {colorama.Fore.LIGHTRED_EX}Created by MrCingo{colorama.Fore.RESET}
                        {colorama.Fore.RED}github.com/limbocingo/yt-downloader/
'''


def download_video(url: str, path: str, format: str) -> str:
    try:
        video = pytube.YouTube(
            url
        )

    except pytube.exceptions.RegexMatchError:
        return 'Unknown video.'

    except pytube.exceptions.AgeRestrictedError:
        return 'This video has age restriction.'

    if format == 'v':
        stream = video.streams.get_by_resolution(resolution='720p')

    elif format == 'a':
        stream = video.streams.filter(only_audio=True).first()

    path = stream.download(output_path=path, filename=video.title +
                    '.mp3' if format != 'v' else video.title + '.mp4')

    return


def option(options: list, input_text: str = '', lower: bool = False) -> str:
    while True:
        user_input = input(input_text).lower()

        if user_input not in options:
            print(f'{colorama.Fore.YELLOW}Uknown option, try again. {colorama.Fore.RESET}')
            continue

        return user_input.lower()


def main():
    finish = None

    os.system('cls' if os.name == 'nt' else 'clear')
    print(LOGO)

    try:
        while True:
            print(f'{colorama.Fore.BLUE}URL of the video you want to download. {colorama.Fore.RESET}')
            url = input('    ')

            print('')
            print(f'{colorama.Fore.BLUE}Format you want to download it. {colorama.Fore.RESET}')
            print(f'{colorama.Fore.CYAN}Audio [a]  Video [v] {colorama.Fore.RESET}')
            format = option(['a', 'v'], input_text='    ', lower=True)

            print('')
            print(f'{colorama.Fore.BLUE}In what path do you want to download it? {colorama.Fore.RESET}')
            print(f'{colorama.Fore.CYAN}Press ENTER if you want in the current path {colorama.Fore.RESET}')
            path = input('    ')

            video = download_video(url, path, format)

            if video:
                print(f'{colorama.Fore.YELLOW}{video} {colorama.Fore.RESET}')
                continue

            if finish == 'c':
                continue

            print(f'{colorama.Fore.BLUE}You\'ve finished? {colorama.Fore.RESET}')
            print(f'{colorama.Fore.CYAN}Yes [y]  No [n]  Don\'t ask again [c] {colorama.Fore.RESET}')
            finish = option(['y', 'n', 'c'], input_text='   ', lower=True)

            if finish == 'y':
                break
    
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{colorama.Fore.GREEN}Thanks for using my script to download YT videos ツ {colorama.Fore.RESET}')


if __name__ == '__main__':
    main()
