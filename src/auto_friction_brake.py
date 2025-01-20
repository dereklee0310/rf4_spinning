from friction_brake import FrictionBrake
import script
import argparse
from multiprocessing import Lock
import pprint

# ------------------ flag name, attribute name, description ------------------ #
ARGS = (
    ("initial", "initial_friction_brake", "_"),
    ("max", "max_friction_brake", "_"),
    ("increase_delay", "increase_delay", "_"),
    ("adjust_delay", "adjust_delay", "_"),
)

class App:
    """Main application class."""

    @script.initialize_setting_and_monitor(ARGS)
    def __init__(self):
        print(self.setting.max_friction_brake)
        self.friction_brake_lock = Lock() # dummy lock
        self.friction_brake = FrictionBrake(
            self.setting, self.monitor, self.friction_brake_lock
        )

    def parse_args(self) -> argparse.Namespace:
        """Cofigure argparser and parse the command line arguments.

        :return dict-like parsed arguments
        :rtype: argparse.Namespace
        """
        parser = argparse.ArgumentParser(
            description="change the friction brake automatically."
        )
        parser.add_argument(
            "-i",
            "--initial",
            metavar="FRICTION_BRAKE",
            type=int,
            help="initial friction brake",
        )
        parser.add_argument(
            "-m",
            "--max",
            metavar="FRICTION_BRAKE",
            type=str,
            help="maximum friction brake",
        )
        parser.add_argument(
            "-I",
            "--increase-delay",
            metavar="SECOND",
            type=float,
            help="delay after changing friction brake",
        )
        parser.add_argument(
            "-a",
            "--adjust-delay",
            metavar="SECOND",
            type=str,
            help="delay before starting to adjust friction brake after a fish is hooked",
        )
        return parser.parse_args()

    def start(self):
        self.friction_brake.monitor_process.start()


if __name__ == "__main__":
    app = App()