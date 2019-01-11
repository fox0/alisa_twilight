#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twilight.settings")
    from django.core.management import execute_from_command_line
    if len(sys.argv) == 1:
        sys.argv.append('runserver')
    execute_from_command_line(sys.argv)
