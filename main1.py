import blessed
import time
import sys

def main():
    term = blessed.Terminal()

    print(term.home + term.clear + term.move_y(term.height // 2))
    print(term.black_on_darkkhaki(term.center('press any key to continue.')))

    dt = 0

    with term.cbreak(), term.hidden_cursor():
        while True:
            inp = term.inkey(timeout=2)
            print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))
            time.sleep(60/1000)


if __name__ == "__main__":
    main()
