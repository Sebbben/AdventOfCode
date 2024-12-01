with open("11.txt") as f:
    data = f.read().split("\n\n")

monkeys = []

for blob in data:
    monkey, items, operation, test, ifTrue, ifFalse = map(lambda x: x.strip(), blob.splitlines())

    mNumber = int(monkey[-2])
    mItems = list(map(int, items.split(":")[1].replace(" ", "").split(",")))

    mOperator = None
    operation = operation.split("= ")[1]
    if "+" in operation:
        operand = int(operation.split(" + ")[1])
        mOperator = lambda x, operand: x + operand
    elif "*" in operation:
        operand = operation.split(" * ")[1]
        if operand == "old":
            mOperator = lambda x, operand: x ** 2
        else:
            operand = int(operand)
            mOperator = lambda x, operand: x * int(operand)
    
    mTest = int(test.split("by ")[1])

    mIfTrue = int(ifTrue[-1])
    mIfFalse = int(ifFalse[-1])

    monkeys.append({
        "number": mNumber,
        "items": mItems,
        "operator": mOperator,
        "operand": operand,
        "test": mTest,
        "testRes": {
            True: mIfTrue,
            False: mIfFalse
        },
        "inspected": 0
    })


for i in range(20):
    for monkey in monkeys:
        for item in monkey["items"]:
            newItem = monkey["operator"](item, monkey["operand"])
            newItem //= 3
            monkeys[monkey["testRes"][newItem%monkey["test"]==0]]["items"].append(newItem)
        monkey["inspected"] += len(monkey["items"])
        monkey["items"] = []

inspectionNumbers = sorted([monkey["inspected"] for monkey in monkeys])
print(inspectionNumbers[-2]*inspectionNumbers[-1])
