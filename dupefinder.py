import hashlib
import os
import argparse

# generate md5 hashes
def generate_md5(filename, chunk_size=4096):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        while chunk := f.read(8192):
            hash.update(chunk)

    return hash.hexdigest()

# create a set of dupes
def create_dupeset(files_dict):
    dupeset = {}
    for key, value in files_dict.items():
        if value not in dupeset:
            dupeset[value] = [key]
        else:
            dupeset[value].append(key)
    return dupeset

# get list of files
def get_filelist(root_dir, verbose=False):
    for currentpath, folders, files in os.walk(root_dir):
        for file in files:
            fullpath = os.path.join(currentpath, file)
            md5 = generate_md5(fullpath)
            if (verbose):
                print(fullpath, end="....  ")
                print(md5)
            files_dict[fullpath] = md5

if __name__ == "__main__":

    # arguments
    parser = argparse.ArgumentParser(description="Get MD5 hash of files in folder")
    parser.add_argument("folder", type=str, help="enter folder name to check")
    parser.add_argument("-v", "--verbose", help="Show MD5 information", action="store_true")
    args = parser.parse_args()
    if args.folder:
        src_folder = args.folder

    files_dict = dict()

    print("Generating checksums...")
    filelist = get_filelist(src_folder, True if args.verbose else False)
    dupeset = create_dupeset(files_dict)

    # show dupes
    print ("The following files are duplicates:")
    for key, value in dupeset.items():
        count = 0
        if len(dupeset[key]) > 1:
            print(key)
            for item in dupeset[key]:
                count = count + 1
                print("{} : {}".format(count, item))