from counter import Counter

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, "Test1"
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
assert counter.get_current() == 10, "Test2"

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, "Test3"
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум
assert counter.get_current() == 7, "Test4"
