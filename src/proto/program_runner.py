def setup(v):
    print("In the main function with value {}".format(v))


def main():
    setup(13)
    print('Hello from main')


if __name__ == "__main__":
    main()
    print('Hello from the current module entry point changed')
