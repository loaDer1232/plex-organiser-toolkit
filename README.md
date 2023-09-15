# plex-organiser-toolkit
This is an open source tool for renaming tv episodes and movies into the plex format,
feel free to use it
## use:
File_Renamer.py [-h] [-v | -q] [-cu] [-l] path name
|positional arguments:| |   
|:-:|:-:|
|path | speicfiys path |  
|name | the new name for the files|

### options:
|short name|long name|use|
|:-:|:-:|:-|
|-h|  --help|        show this help message and exit|
|-v|  --verbose|     incresses output verbosity|
|-q|  --quiet|       removes console feedback|
|-cu| --cleanup|     removes files not in list of approved video files|
|-l|  --log|         outputs file changes to log file|
|-m|  --movies|      removes episode and season and names in movie format|

the log file is output into the working directory:   
>PATH\log.txt

when using cleanup the allowed file types are:   
|||
|:-:|:-:|
|mkv|avi|
|mp4|asf|
|mov|srt|
|wmv|MPEGTS|


## Style guide: 
1. Varibles should be in camelCase and have type hints
2. Functions are camelCase with _ between each word and have type hints
3. Classes have capitals at the start and for each word and have descriptions and Attributes
4. Identation should be done with tabs     

Example
```
def example_Function(foo: int, bar: str)-> str:
    fooBar: str = str(foo) + bar
    return fooBar

class ExampleClass:
    ''' this is an example
    Attributes:
    this: this is fake
    '''
```
