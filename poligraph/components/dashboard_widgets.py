"""
Dashboard widget components for Poligraph.

This module contains reusable widget components used in the dashboard,
such as statistics cards, activity feeds, and action panels.
"""

import reflex as rx
from ..styles.styles import CARD_STYLE

def statistics_card():
    """Create a statistics display card."""
    return rx.box(
        rx.heading("Statistics", size="md"),
        rx.text("Your stats here"),
        style=CARD_STYLE,
    )

def activity_card():
    """Create a recent activity display card."""
    return rx.box(
        rx.heading("Recent Activity", size="md"),
        rx.text("Activity feed here"),
        style=CARD_STYLE,
    )

def actions_card():
    """Create a quick actions card."""
    return rx.box(
        rx.heading("Quick Actions", size="md"),
        rx.text("Action buttons here"),
        style=CARD_STYLE,
    ) 