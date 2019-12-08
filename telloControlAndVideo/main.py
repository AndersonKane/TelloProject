import tello
from tello_control_ui import TelloUI


def main():

    drone = tello.Tello('', 8889)
    vplayer = TelloUI(drone,"./img/")
    # It will starts tkimage loop
    vplayer.root.mainloop()

if __name__ == "__main__":
    main()
