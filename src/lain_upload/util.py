import argparse
import re


def expire_after_type(value):
    if not re.fullmatch(r"\d+h", value):
        raise argparse.ArgumentTypeError(
            f"invalid format: '{value}'. must be like '12h'."
        )
    return value
