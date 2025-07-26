import blessed
import time
import sys

def main():
    term = blessed.Terminal()

    print(term.home + term.clear + term.move_y(term.height))

    dt = 0

    with term.cbreak(), term.hidden_cursor(), term.fullscreen():
        while True:
            t = []
            while len(t) != 2:
                inp = term.inkey(timeout=2)
                if (ord(inp) >= 97 and ord(inp) <= 122) or (ord(inp) >= 65 and ord(inp) <= 90):
                    t.append(inp)
                #inp = input("give input\n")
        
        print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))
        print(term.home + term.clear + term.move_y(term.height))


if __name__ == "__main__":
    main()
