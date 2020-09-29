"""
    Fetches the testcase related to problem statement
"""
import argparse
from pathlib import Path
import requests
from bs4 import BeautifulSoup # type: ignore

def get_parser():
    """
        Command line arguments
    """
    parser = argparse.ArgumentParser("Program to fetch testcases from codeforces contest")
    parser.add_argument('--idx', '-i', type=str, help="relative url of problem description.")
    parser.add_argument('--contest', '-c', type=str, help="contest url(name)")
    return parser


def write_into_file(data: BeautifulSoup, direc: Path) -> None:
    """
        Stores the data to file
    """
    for idx, i in enumerate(data, start=1):
        with open(direc / (str(idx).zfill(3) + '.txt'), 'w') as file:
            case = i.find("pre").text.lstrip()
            file.write(case)


def main():
    """
        Fetches testcases from web, Creates directory and stores locally
    """
    # pylint: disable-msg=too-many-locals
    idx = 'A'
    contest = '1332'

    args = get_parser().parse_args()

    if args.contest:
        contest = args.contest
    if args.idx:
        idx = args.idx

    problem = "https://codeforces.com/contest/" + contest +"/problem/" + idx
    response = requests.get(problem)
    if response.status_code != 200:
        print("Invalid URL")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    BASE_DIR = Path(__file__).resolve().parent
    TESTCASES_DIR = BASE_DIR / 'testcases'
    TESTCASES_DIR.mkdir(parents=True, exist_ok=True)
    INP_DIR = TESTCASES_DIR / idx / 'inp'
    OUT_DIR = TESTCASES_DIR / idx / 'op'

    INP_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    in_p = soup.findAll("div", {"class": "input"})
    o_p = soup.findAll('div', {'class': 'output'})

    write_into_file(in_p, INP_DIR)
    write_into_file(o_p, OUT_DIR)

if __name__ == "__main__":
    main()
