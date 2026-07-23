"""
==========================================================
File        : report_generator.py
Description : Displays reports in table format
==========================================================
"""

from tabulate import tabulate


# ==========================================================
# Display Table
# ==========================================================

def display_table(records, headers):

    if not records:

        print("\nNo Records Found.")

        return

    print()

    print(

        tabulate(

            records,

            headers=headers,

            tablefmt="grid"

        )

    )


# ==========================================================
# Print Heading
# ==========================================================

def print_heading(title):

    print()

    print("=" * 80)

    print(title.center(80))

    print("=" * 80)