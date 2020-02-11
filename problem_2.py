
import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    
    result = []
    for file in os.listdir(path):        
        if os.path.isfile(os.path.join(path,file)) and file.endswith(suffix):
            #print(file)
            result.append(os.path.join(path,file))
        if os.path.isdir(os.path.join(path,file)):
            result.extend ( find_files(suffix, os.path.join(path,file)) )

    return result

print(".c files:")
print( find_files(".c","./testdir") ,"\n")

print(".h files:")
print( find_files(".h","./testdir") ,"\n")

print(".c files from top directory")
print( find_files(".c",".") ,"\n")

print(".c files from sub directory 1")
print( find_files(".c","./testdir/subdir1") ,"\n")

print(".c files from sub directory 2")
print( find_files(".c","./testdir/subdir2") ,"\n")

print(".c files from sub directory 3")
print( find_files(".c","./testdir/subdir3") ,"\n")

print(".c files from sub directory 4")
print( find_files(".c","./testdir/subdir4") ,"\n")

print(".c files from sub directory 5")
print( find_files(".c","./testdir/subdir5") ,"\n")