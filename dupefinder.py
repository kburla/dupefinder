import hashlib
import os
import argparse

parser = argparse.ArgumentParser(description="Get MD5 hash of files in folder")
parser.add_argument("folder", type=str, help="enter folder name to check")
args = parser.parse_args()
if args.folder:
    src_folder = args.folder


def generate_md5(filename, chunk_size=4096):

    hash = hashlib.md5()
    with open(filename, "rb") as f:
        while chunk := f.read(8192):
            hash.update(chunk)

    return hash.hexdigest()


if __name__ == "__main__":

    files_dict = dict()

    for path, dirs, files in os.walk(src_folder):
        print("Generating checksums...")
        for file_name in files:
            files_dict[file_name] = generate_md5(os.path.join(src_folder, file_name))

    # show duplicates
    dupeset = {}

    # create a set of dupes
    for key, value in files_dict.items():
        if value not in dupeset:
            dupeset[value] = [key]
        else:
            dupeset[value].append(key)

    # show only the dupes
    print ("The following files are duplicates:")
    for key, value in dupeset.items():
        count = 0
        if len(dupeset[key]) > 1:
            print(key)
            for item in dupeset[key]:
                count = count + 1
                print("{} : {}".format(count, item))

    # with open(os.path.join(src_folder, "checksum.txt"), "w") as f:
    #     for key, value in files_dict.items():
    #         f.write("{} : {}\n".format(value, key))
    #         print("{} : {}".format(value, key))
