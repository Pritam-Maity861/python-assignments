files = [
    "resume.pdf",
    "photo.jpg",
    "report.pdf",
    "data.csv",
    "image.png",
    "notes.txt",
    "file",
    "README",
    "archive.tar.gz"
]


def get_file_extension(filename):
    if "." not in filename:
        return None

    extension = filename.rsplit(".", 1)[1]

    if not extension:
        return None

    return extension.lower()


def analyze_extensions(files):
    result = {}
    for filename in files:
        extension = get_file_extension(filename)

        if extension is None:
            continue

        if extension in result:
            result[extension] += 1
        else:
            result[extension] = 1

    return result


print(analyze_extensions(files))
