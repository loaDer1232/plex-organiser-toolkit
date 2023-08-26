import os

strSeason: str
rootPath: str = input(r"Enter the path:  ") #Here put the path of your folder where your images are stored
newName: str = input("Enter name: ") #Here, enter the name you want your images to have
totalEpisodes: int = 0
season: int = 1

def iFormat(i: int)-> str:
    if i < 10:
        return f"0{i}"
    else:
        return str(i)

def season_Format(i: int)-> str:
    if i < 10:
        return f"0{i}"
    else:
        return str(i)

def nested(subDir: list[str]):
    global season
    for i in range(len(subDir)):
        subPath: str = os.path.join(path,subDir[i])
        not_Nested(subPath)
        season += 1


def not_Nested(fullPath: str):
    global totalEpisodes
    episode: int = 1
    for file in os.listdir(fullPath):
        ext: str = os.path.splitext(file)
        newFileName = f"{newName} S{season_Format(season)}E{iFormat(episode)}{ext[1]}" 
        os.rename(os.path.join(fullPath, file), os.path.join(fullPath, newFileName))
        episode += 1
    totalEpisodes += (episode - 1)


for path, subDir, files in os.walk(rootPath):
    if len(subDir) == 0:
       not_Nested(rootPath)
    else:
        nested(subDir)
    input(f"Renamed {totalEpisodes} files in {season - 1} folders!!")
    exit()