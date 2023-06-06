"""==================================================================================================================***
***==  MONKEY MANIFEST  =============================================================================================***
***                                                                                                                  ***
***    The Monkey Manifest houses centralized configuration of automation profiles (monkeys).                        ***
***                                                                                                                  ***
***    Undefined props will default based on `storage/internal/defaults/monkey-config-defaults.yaml`.                ***
***    Monkey props defined in your .env will override the framework defaults.                                       ***
***                                                                                                                  ***
***=================================================================================================================="""


class ExamplePythonClass:
    @staticmethod
    def __post_init__():
        # General
        EXAMPLE_PYTHON_PROP = "EXAMPLE_PYTHON_PROP"
        INTENTION = "See how the header-comment works in a real class"

        # Admissions
        ADMISSION = "I'm kind of tired and slap-happy and I'll be sure to remove this silliness in favor of example " \
                    "class attributes that actually look like real Python code. I mean that's kind of the point right."
        ADMISSION_SECONDARY = "I'm totally not going to remove this silliness. It actually looks like a legit enough " \
                              "example to be honest."

        # References
        # Note: REALLY A MUCH BETTER PAN FLICK THAN THE EMBARRASSINGLY TRITE RECENT DISNEY OFFERING
        ENABLE_REFERENCES = True
        LOAD_REFERENCE_LIBRARY = ["UNDERRATED_FILMS", "PIRATE_ADJACENT"]
        LOOKIE_LOOKIE = "I'VE GOT HOOKED ☠️🪝🧚‍🐊🕰️"

        # Base-Covering
        INCLUSION_OF_INT = 42
        NUMBER_OF_TRIES = 1
        NUMBER_OF_PROOFREADS = 0

    @staticmethod
    def predictions():
        """
        This function returns a dictionary of "predictions" about the future.
        """
        PREDICTIONS_ENABLED = True
        REALITY_LEVEL_PERCENTAGE = 0.96
        PREDICTION_OPT_ONE = "I leave this in either because I still think its funny or because I forget. You are " \
                             "weird enough to have read this far (don't blame me, you're in the driver's seat here " \
                             "bud) and my confidence that I would leave it in the final version seems legit, " \
                             "unless you're enough of a psychopath to *still* be reading this. I mean, I probably " \
                             "never even read it again myself, but no judgement."
        PREDICTION_OPT_TWO = "I remove this because its not funny and I'm not that forgetful. You never know that I " \
                             "was exaggerating my confidence that I would decide to leave it in"
        PREDICTION_OPT_THREE = False

        return {
            'PREDICTIONS_ENABLED': PREDICTIONS_ENABLED,
            'REALITY_LEVEL_PERCENTAGE': REALITY_LEVEL_PERCENTAGE,
            'PREDICTION_OPT_ONE': PREDICTION_OPT_ONE,
            'PREDICTION_OPT_TWO': PREDICTION_OPT_TWO,
            'PREDICTION_OPT_THREE': PREDICTION_OPT_THREE,
        }
