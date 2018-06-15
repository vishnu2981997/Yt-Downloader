import time
from pytube import YouTube


def main():
    """
    :return: Null
    """

    # Getting the url of the desired video

    url = input("Enter the video url : ")
    time.sleep(2)

    # Getting the desired format of the video for downloading

    resolution = input("Enter the format : ")
    time.sleep(2)

    # Loading the url

    try:
        tube = YouTube(url)
    except:
        print("Problem loading url")

    # Fetching all responsive formats for download

    formats = tube.streams.filter(progressive=True).all()
    time.sleep(2)

    # Displaying title of the url

    print("Downloading "+tube.title)
    time.sleep(2)

    print("Download may take time depending on your internet speed.")
    time.sleep(2)

    print("Please be patient while the video is being downloaded.")
    time.sleep(2)

    print("Do not exit the program or turn off your wifi while the video is being downloaded")
    time.sleep(2)

    # Checking for the desired format for download

    try:

        for i in formats:

            temp = str(i)

            if resolution in temp:

                stream = i
                stream.download()

                print("Download completed")

                break
    except:

        print("Problem fetching streams. Check you network connection")

if __name__ == "__main__":
    main()
