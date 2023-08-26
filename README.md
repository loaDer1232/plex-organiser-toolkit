# plex-organiser-tools
this is an open source tool for name tv episode into the plex format
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
|-h| --help|         show this help message and exit|
|-v| --verbose|      incresses output verbosity|
|-q| --quiet|        removes console feedback|
|-cu| --cleanup|     removes files not in list of approved video files|
|-l| --log|   outputs file changes to log file|

## style guide: 
1. varibles should be in camelCase and have type hints
2. functions are camelCase with _ between each word and have type hints
3. classes have capatilas ate the start and for each word and have descriptions and Attributes
4. identation should be done with tabs     

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
