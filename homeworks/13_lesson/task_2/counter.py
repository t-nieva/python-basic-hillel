class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        if not (min_value <= current <= max_value):
            raise ValueError("Initial current must be within min and max bounds.")
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if not (self.min_value <= start <= self.max_value):
            raise ValueError("Current value must be within min and max bounds.")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("max_value cannot be less than min_value.")
        if self.current > max_max:
            raise ValueError("Current value is out of the new max bound.")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("min_value cannot be greater than max_value.")
        if self.current < min_min:
            raise ValueError("Current value is out of the new min bound.")
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("The maximum allowed value has been reached.")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("The minimum allowed value has been reached.")
        self.current -= 1

    def get_current(self):
        return self.current
