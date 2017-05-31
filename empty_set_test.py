def test(key, visited=set()):
    visited.add(key)
    return visited

print("test1 - set()")
print(test("x"))
print(test("y"))

def test2(key, visited=None):
    if visited == None:
        visited = set()
    visited.add(key)
    return visited

print("\ntest2 - None")
print(test2("x"))
print(test2("y"))
