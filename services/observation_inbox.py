"""
Observation Inbox Service
"""

from pathlib import Path


INBOX_PATH = Path("inbox")


def get_pending_observations():
    """Return all observation JSON files waiting in the inbox."""

    return sorted(INBOX_PATH.glob("*.json"))