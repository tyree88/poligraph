"""
Base state management for Poligraph.

This module defines the base State class that handles the application's
state management. It serves as the foundation for all state-related
operations in the application.
"""

import reflex as rx

class State(rx.State):
    """
    Base state class for the Poligraph application.
    
    This class manages the global application state and provides
    methods for state updates and data management.
    """
    # Add state variables for dashboard data
    statistics: dict = {}
    recent_activity: list = []
    quick_actions: list = []

    def update_statistics(self, new_stats: dict):
        """Update dashboard statistics."""
        self.statistics = new_stats

    def update_activity(self, new_activity: list):
        """Update recent activity feed."""
        self.recent_activity = new_activity

    def update_actions(self, new_actions: list):
        """Update available quick actions."""
        self.quick_actions = new_actions 