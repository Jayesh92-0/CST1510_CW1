responses = [
    "  VERY SATISFIED  ",
    "somewhat happy   ",
    "  NOT Happy  ",
    "   NEUTRAL",
    "  dissatisfied  "
]

for response in responses:
    cleaned = response.strip().lower()
    print(cleaned)
    