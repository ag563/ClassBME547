import requests


def get_branches():
    r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
    print(r)
    print(type(r))


if __name__ == "__main__":
    get_branches()