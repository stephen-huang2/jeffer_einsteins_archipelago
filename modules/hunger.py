class Hunger:
    """Manages the player's hunger, tracking points that deplete over time."""

    def __init__(self, max_points=30):
        self.max_points = max_points      # Maximum hunger points the player can have
        self.current_points = max_points  # Current hunger points, starts at max

    def deplete(self, amount=1):
        """Reduce hunger by amount, returns True if still alive, False if starved."""
        self.current_points -= amount

        # Clamp to zero to prevent negative hunger points
        if self.current_points < 0:
            self.current_points = 0

        return self.current_points > 0

    def eat(self, food_name):
        """Consume food and restore hunger points."""
        # Maps food names to their hunger restoration values
        food_values = {
            "Pork": 5,
            "Bread": 3,
            "Apple": 1,
        }

        # Extract food name without item number (e.g. "1. Pork" -> "Pork")
        food_type = food_name.split(". ")[-1] if ". " in food_name else food_name

        if food_type in food_values:
            restore_amount = food_values[food_type]
            self.current_points += restore_amount

            # Clamp to max to prevent exceeding the hunger cap
            if self.current_points > self.max_points:
                self.current_points = self.max_points

            return True, restore_amount

        # Food not recognised, return failure with zero restoration
        return False, 0

    def get_status(self):
        """Return current hunger status."""
        percentage = (self.current_points / self.max_points) * 100
        return (
        return (f"Hunger: {self.current_points}/"
                + f"{self.max_points} ({percentage:.0f}%)")

    def is_starving(self):
        """Check if hunger is fully depleted."""
        return self.current_points <= 0