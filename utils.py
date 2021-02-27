import pandas as pd


def configure_pandas() -> None:
    """Prettify pandas output."""
    options = {
        "display": {
            "max_columns": None,
            "max_colwidth": 20,
            "max_rows": 40,
            "max_seq_items": 10,  # Max length of printed sequence
            "float": "{:.3f}".format,
            "expand_frame_repr": False,  # Don't wrap to multiple pages
            "show_dimensions": True,
        }
    }

    for category, option in options.items():
        for op, value in option.items():
            pd.set_option(f"{category}.{op}", value)
