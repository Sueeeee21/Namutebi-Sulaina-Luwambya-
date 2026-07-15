class UnderageDriverException(Exception):
    def __init__(self, age):
        super().__init__(f"Must be 18 or older to drive in Uganda. You are {age}.")

def drive(age):
    if age < 18:
        raise UnderageDriverException(age)
    print(f"Age {age}: Allowed to drive!")

for age in [15, 18, 21]:
    try:
        drive(age)
    except UnderageDriverException as e:
        print(f"Age {age}: {e}")