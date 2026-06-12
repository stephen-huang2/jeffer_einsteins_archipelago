class Hunger:
    def __init__(self, max_points=30):
        self.max_points = max_points
        self.current_points = max_points
    
    def deplete(self, amount=1):
        """Reduce hunger by amount, returns True if still alive, False if starved"""
        self.current_points -= amount
        if self.current_points < 0:
            self.current_points = 0
        return self.current_points > 0
    
    def eat(self, food_name):
        """Consume food and restore hunger points"""
        food_values = {
            "Pork": 5,
            "Bread": 3,
            "Apple": 1
        }
        
        # Extract food name without item number
        food_type = food_name.split(". ")[-1] if ". " in food_name else food_name
        
        if food_type in food_values:
            restore_amount = food_values[food_type]
            self.current_points += restore_amount
            if self.current_points > self.max_points:
                self.current_points = self.max_points
            return True, restore_amount
        return False, 0
    
    def get_status(self):
        """Return current hunger status"""
        percentage = (self.current_points / self.max_points) * 100
        return f"Hunger: {self.current_points}/{self.max_points} ({percentage:.0f}%)"
    
    def is_starving(self):
        """Check if hunger is depleted"""
        return self.current_points <= 0
