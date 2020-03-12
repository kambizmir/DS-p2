
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
    try:
        
        for file in os.listdir(path):        
            if os.path.isfile(os.path.join(path,file)) and file.endswith(suffix):            
                result.append(os.path.join(path,file))
            if os.path.isdir(os.path.join(path,file)):
                result.extend ( find_files(suffix, os.path.join(path,file)) )

    except Exception as e:
        print(str(e))

    return result


print("Happy path tests:\n")
print(".c files:")
print( find_files(".c","./testdir") )

print(".h files:")
print( find_files(".h","./testdir") )

print(".c files from top directory")
print( find_files(".c","."))

print(".c files from sub directory 1")
print( find_files(".c","./testdir/subdir1") )

print(".c files from sub directory 2")
print( find_files(".c","./testdir/subdir2"))

print(".c files from sub directory 3")
print( find_files(".c","./testdir/subdir3"))

print(".c files from sub directory 4")
print( find_files(".c","./testdir/subdir4"))

print(".c files from sub directory 5")
print( find_files(".c","./testdir/subdir5") )

print("\nEdge case: nonexisting suffix, result should be empty list\n")

print(".x files:")
print( find_files(".x","./testdir") ,"\n")


print("\nEdge case: nonexisting path, should show graceful message and empty result\n")

print(".c files:")
print( find_files(".c","./testdir1") ,"\n")



print("\nEdge case: nonexisting suffix, nonexisting path, should show graceful message and empty result\n")

print(".pdf files:")
print( find_files(".y","./testdir2") ,"\n")