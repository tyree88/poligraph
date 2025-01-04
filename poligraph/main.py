"""
Main application entry point for Poligraph.

This module initializes the Reflex application and sets up the routing.
Poligraph is a dashboard application for analyzing and visualizing 
social media data from BlueSky.
"""

import reflex as rx
from .pages.dashboard import dashboard

# Create app instance and add page routes
app = rx.App()
app.add_page(dashboard, route="/") 