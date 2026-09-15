from Business.goncourt import Goncourt

def main() -> None:
    goncourt : Goncourt = Goncourt()

    goncourt.init_static()

if __name__ == "__main__":
    main()