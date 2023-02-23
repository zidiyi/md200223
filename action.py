import os
import string
import random


def duplicate_and_rename_md_files(times=3, nameLen=30):
    for filename in os.listdir("."):
        if filename.endswith(".md"):
            # Duplicate the file three times
            for _ in range(times):
                new_filename = (
                    "".join(
                        random.choices(
                            string.ascii_lowercase + string.digits, k=nameLen
                        )
                    )
                    + ".md"
                )
                os.system(f"cp {filename} {new_filename}")


duplicate_and_rename_md_files()
