"""
Dashboard page for Poligraph.

This module contains the main dashboard view that displays analytics
and visualizations for BlueSky social media data. It includes various
widgets for statistics, recent activity, and quick actions.
"""

import reflex as rx
from ..components.navbar import navbar
from ..components.sidebar import sidebar
from ..components.dashboard_widgets import statistics_card, activity_card, actions_card
from ..styles.styles import CONTENT_STYLE

def dashboard():
    """
    Creates the main dashboard view with statistics and activity feeds.
    
    Returns:
        rx.Component: A Reflex component representing the dashboard page
    """
    return rx.box(
        navbar(),
        rx.hstack(
            sidebar(),
            rx.box(
                rx.heading("Dashboard Overview"),
                rx.text("Welcome to Poligraph Dashboard"),
                rx.spacer(),
                rx.simpleGrid(
                    statistics_card(),
                    activity_card(),
                    actions_card(),
                    columns=[3],
                    spacing="4",
                ),
                style=CONTENT_STYLE,
            ),
        ),
    ) 