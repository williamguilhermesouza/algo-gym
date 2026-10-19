import os

topics = ["sort", "search", "list", "sets"]


def main() -> None:
    print("=" * 10 + "Generating ring" + "=" * 10)

    try:
        for topic in topics:
            if not os.path.exists(topic):
                os.mkdir(os.path.join(".", topic))
    except:
        print("Failed creating directories")
        exit(-1)

    print("=" * 10 + " Ring topics created " + "=" * 10)
    print("=" * 10 + " Completed! " + "=" * 10)
