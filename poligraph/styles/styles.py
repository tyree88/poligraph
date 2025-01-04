"""
Global styles for the Poligraph application.

This module contains style definitions that are used across the application
to maintain consistent look and feel. Styles are defined as dictionaries
that can be passed to Reflex components.
"""

# Navigation bar styles - fixed at top of the page
NAVBAR_STYLE = {
    "width": "100%",
    "height": "4em",
    "padding": "1em",
    "background_color": "#f8f9fa",
    "display": "flex",
    "align_items": "center",
    "justify_content": "space-between",
}

# Sidebar styles - fixed on the left side
SIDEBAR_STYLE = {
    "width": "250px",
    "height": "100vh",
    "background_color": "#f8f9fa",
    "padding": "1em",
}

# Main content area styles - adjusts for navbar and sidebar
CONTENT_STYLE = {
    "margin_left": "250px",
    "padding": "2em",
}

# Card styles for dashboard widgets
CARD_STYLE = {
    "padding": "1em",
    "background": "white",
    "border_radius": "md",
    "box_shadow": "lg",
} 