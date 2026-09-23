from itertools import combinations
from config import COURSE_FEES


BUDGET = 30000


def find_combinations():
    courses = list(COURSE_FEES.keys())

    for r in range(1, len(courses) + 1):
        for combo in combinations(courses, r):
            total = sum(COURSE_FEES[c] for c in combo)

            if total <= BUDGET:
                print(
                    f"{combo} -> Rs.{total:,} "
                    f"(within budget)"
                )
            else:
                print(
                    f"{combo} -> Rs.{total:,} "
                    f"(over budget)"
                )


print(f"Budget: Rs.{BUDGET:,}")
print()
find_combinations()