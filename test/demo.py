import curses, curses_ex

def demo(scrn):
    # define character 'a' as keycode 600.
    curses_ex.define_key(b'a', 600)
    n = 0
    while True:
        c = scrn.getch()
        scrn.addstr(n, 0, str(c))
        scrn.clrtoeol()
        n = 0 if n > 10 else n+1

if __name__ == '__main__':
    curses.wrapper(demo)

