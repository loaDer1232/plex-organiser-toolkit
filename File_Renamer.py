import os
import argparse

parser = argparse.ArgumentParser(description="plex formating tool to fix tv file names")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help="incresses output verbosity", action="store_true")
group.add_argument("-q", "--quiet", help="removes console feedback", action="store_true")
parser.add_argument("-cu", "--cleanup", help="removes files not in list of approved video files", action="store_true")
parser.add_argument("-l", "--log", help="outputs file changes to log file", action="store_true")
parser.add_argument("-m", "--movies", help="removes the season and epsiode for use on movies", action="store_true")
parser.add_argument("path", help="speicfiys path")
parser.add_argument("name", help="the new name for the files")
args = parser.parse_args()


logStr: str = ""
rootPath: str = args.path
newName = args.name
totalEpisodes: int = 0
season: int = 1
filesDeleted: int = 0
validFormats: list[str] = ['.mkv', ".asf", ".mp4" ".srt", "avi", "mov", "wmv", "mpegts", ""]

def log():
    with open(f'{rootPath}\log.txt','a') as log:
        log.write(logStr)

def cleaner(fullPath: str):
    global logStr, filesDeleted
    for file in os.listdir(fullPath):
        ext: str = os.path.splitext(file)
        if ext in validFormats:
            continue
        os.remove(os.path.join(fullPath, file))
        if args.verbose:
            print(f"deleted {file}")
        logStr += f"deleted {file}\n"
        filesDeleted += 1


def episode_Format(i: int)-> str:
    if i < 10:
        return f"0{i}"
    else:
        return str(i)

def season_Format(i: int)-> str:
    if i < 10:
        return f"0{i}"
    else:
        return str(i)
    
def movieFormat(i: int)-> str:
    if i == 1:
        return ""
    else:
        return f" {i}"

def namer(episode: int, ext: str)-> str:
    if args.movies:
        return f"{newName}{movieFormat(episode)}{ext}"
    else:
        return f"{newName} S{season_Format(season)}E{episode_Format(episode)}{ext}" 

def nested(subDir: list[str]):
    global season
    for i in range(len(subDir)):
        subPath: str = os.path.join(path,subDir[i])
        not_Nested(subPath)
        if args.cleanup:
            cleaner(subDir)
        season += 1


def not_Nested(fullPath: str):
    global totalEpisodes, logStr
    episode: int = 1
    for file in os.listdir(fullPath):
        ext: str = os.path.splitext(file)
        if ext[1] == '':
            continue
        newFileName = namer(episode, ext[1])
        os.rename(os.path.join(fullPath, file), os.path.join(fullPath, newFileName))
        if args.verbose:
            print(f"renamed {file} to {newFileName}")
        if args.cleanup:
            cleaner(fullPath)
        logStr += f"renamed {file} to {newFileName}\n"
        episode += 1
    totalEpisodes += (episode - 1)

for path, subDir, files in os.walk(rootPath):
    if len(subDir) == 0:
       not_Nested(rootPath)
    else:
        nested(subDir)
    if args.quiet:
        exit()
    if args.log:
        logStr += f"Renamed {totalEpisodes} files and {filesDeleted} deleted in {season - 1} folders!!"
        log()
    input(f"Renamed {totalEpisodes} files and {filesDeleted} deleted in {season - 1} folders!!")
    exit()