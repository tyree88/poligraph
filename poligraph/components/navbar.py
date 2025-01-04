"""
Navigation bar component for Poligraph.

This component provides the top navigation bar with the application title
and main navigation links. It's designed to be consistent across all pages.
"""

import reflex as rx
from ..styles.styles import NAVBAR_STYLE

def navbar():
    """
    Creates the navigation bar with application title and main navigation links.
    
    Returns:
        rx.Component: A Reflex component representing the navigation bar
    """
    return rx.box(
        rx.heading("Poligraph", size="lg"),
        rx.spacer(),
        rx.hstack(
            rx.link("Dashboard", href="/"),
            rx.link("About", href="/about"),
            spacing="4em",
        ),
        style=NAVBAR_STYLE,
    ) 