from day08.forest import Forest


f = open('input.txt', 'r', encoding="utf-8")
forest = Forest(f)
forest._process_input()
print(forest.total_visible())
