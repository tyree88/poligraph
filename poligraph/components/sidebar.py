"""
Sidebar component for Poligraph.

This component provides the main navigation sidebar with links to different
sections of the application. It remains visible on all pages for easy navigation.
"""

import reflex as rx
from ..styles.styles import SIDEBAR_STYLE

def sidebar():
    """
    Creates the sidebar with navigation links to different sections.
    
    Returns:
        rx.Component: A Reflex component representing the sidebar
    """
    return rx.box(
        rx.vstack(
            rx.heading("Menu", size="md"),
            rx.link("Overview", href="/"),
            rx.link("Analytics", href="/analytics"),
            rx.link("Reports", href="/reports"),
            align_items="stretch",
            spacing="1em",
        ),
        style=SIDEBAR_STYLE,
    ) 