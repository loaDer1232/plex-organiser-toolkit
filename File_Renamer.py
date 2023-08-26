import os

strSeason: str
rootPath: str = input(r"Enter the path:  ") #Here put the path of your folder where your images are stored
newName: str = input("Enter name: ") #Here, enter the name you want your images to have


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


totalEpisodes: int = 0
season: int = 1
for path, subDir, files in os.walk(rootPath):
    for i in range(len(subDir)):
        subPath: str = os.path.join(path,subDir[i])
        episode: int = 1
        for file in os.listdir(subPath):
            ext: str = os.path.splitext(file)
            newFileName = f"{newName} S{season_Format(season)}E{iFormat(episode)}{ext[1]}" 
            os.rename(os.path.join(subPath, file), os.path.join(subPath, newFileName))
            episode += 1
        totalEpisodes += (episode - 1)
        season += 1
    input(f"Renamed {totalEpisodes} files in {season - 1} folders!!")
    exit()