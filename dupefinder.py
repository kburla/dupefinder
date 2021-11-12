import hashlib
import os

src_folder = "md5test"


def generate_md5(filename, chunk_size=4096):

    hash = hashlib.md5()
    with open(filename, "rb") as f:
        while chunk := f.read(8192):
            hash.update(chunk)

    return hash.hexdigest()

if __name__ == "__main__":

    files_dict = dict()

    for path, dirs, files in os.walk(src_folder):
        for file_name in files:
            # print("Generating checksum for {}".format(file_name))
            files_dict[file_name] = generate_md5(os.path.join(src_folder, file_name))

    print(files_dict)

    # with open(os.path.join(src_folder, "checksum.txt"), "w") as f:
    #     for key, value in md5_dict.items():
    #         f.write("{} : {}\n".format(value, key))
    #         print("{} : {}".format(value, key))
