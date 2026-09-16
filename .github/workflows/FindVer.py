import os
import re

# Version folders are v<major>.<minor>[.<patch>[.<build>]], optionally carrying a
# pre-release suffix such as -rc1. Two naming schemes live side by side: up to
# v2.17 a line was v2.<PG major> (v2.17) holding releases v2.<PG major>.<minor>
# (v2.17.0), while from v2.18.4 on a line is v2.<PG major>.<PG minor> (v2.18.4)
# holding releases v2.<PG major>.<PG minor>.<minor> (v2.18.4.0), matching the
# branches and tags in the agensgraph repository.
VERSION_PATTERN = re.compile(r'v(\d+(?:\.\d+){1,3})(-rc\d+)?$')

def extract_version(folder_name):
    """Extracts version numbers as a padded tuple of integers for proper comparison."""
    match = VERSION_PATTERN.match(folder_name)
    if not match:
        return None
    numbers = [int(x) for x in match.group(1).split('.')]
    return tuple(numbers + [0] * (4 - len(numbers)))

def is_prerelease(folder_name):
    """Tells release candidates apart: they get an image of their own,
    but latest only ever tracks a full release."""
    match = VERSION_PATTERN.match(folder_name)
    return bool(match and match.group(2))

def get_subfolders(base_dir):
    return [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

def find_highest_release(base_dir='.'):
    """Finds the highest full release across every line.

    Release candidates are held back here alone, so that latest never points at
    an unreleased version; the per-OS workflows still build them.
    """
    releases = []
    for line in get_subfolders(base_dir):
        if extract_version(line) is None:  # skips 'archive' and anything unversioned
            continue
        for release in get_subfolders(os.path.join(base_dir, line)):
            version = extract_version(release)
            if version is None or is_prerelease(release):
                continue
            releases.append((version, line, release))
    return max(releases) if releases else None

if __name__ == "__main__":
    highest = find_highest_release()
    if highest is None:
        raise SystemExit("FindVer: no release folder found")
    _, highest_line, highest_release = highest
    print(f"./{highest_line}/{highest_release}/")
