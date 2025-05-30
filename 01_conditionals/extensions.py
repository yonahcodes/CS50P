# Prompt user for file name & separate suffix
def main():
    file = input("File name: ").lower().strip().rpartition(".")
    suffix = file[2]
    print(media_type(suffix), end="")


def media_type(suffix):
    # If suffix is on the list, convert into media type
    if suffix == "gif" or suffix == "png":
        media = f"image/{suffix}"
    elif suffix == "jpg" or suffix == "jpeg":
        media = "image/jpeg"
    elif suffix == "pdf" or suffix == "zip":
        media = f"application/{suffix}"
    elif suffix == "txt":
        media = "text/plain"
    # If suffix is not on the list, output application/octet-stream
    else:
        media = "application/octet-stream"
    return media


main()
