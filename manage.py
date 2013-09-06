#!/usr/bin/env python
import os, sys, settings

if __name__ == "__main__":
    from django.core.management import execute_manager, execute_from_command_line
    execute_manager(settings)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cat.settings")
    execute_from_command_line(sys.argv)
