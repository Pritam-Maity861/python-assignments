class FileExtensionAnalyzer:
    def __init__(self, files):
        self.files = files

    def get_file_extension(self, filename):
        if "." not in filename:
            return None
        return filename.rsplit(".", 1)[1].lower()

    def analyze_extensions(self):
        result = {}
        for filename in self.files:
            extension = self.get_file_extension(filename)
            if extension is None:
                continue

            if extension in result:
                result[extension] += 1
            else:
                result[extension] = 1

        return result


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

analyzer = FileExtensionAnalyzer(files)

print(analyzer.analyze_extensions())
