def show_head_tail(scores):
    if scores == []:
        print("The list is empty.")
        return

    head = scores[0]
    tail = scores[1:]

    print("Head:", head)
    print("Tail:", tail)


# Recursive sum
def recursive_sum(scores):
    if scores == []:          # Base case
        return 0
    return scores[0] + recursive_sum(scores[1:])


# ascending order
def is_sorted(scores):
    if len(scores) <= 1:      # Base case
        return True

    if scores[0] > scores[1]:
        return False

    return is_sorted(scores[1:])


# Find largest score recursively
def largest_score(scores):
    if len(scores) == 1:      # Base case
        return scores[0]

    largest_rest = largest_score(scores[1:])

    if scores[0] > largest_rest:
        return scores[0]
    else:
        return largest_rest


# Main Program

scores = list(map(int, input("Enter scores separated by spaces: ").split()))

print("\n--- Score List Explorer ---")

show_head_tail(scores)

print("Recursive Sum:", recursive_sum(scores))

if is_sorted(scores):
    print("The scores are sorted in ascending order.")
else:
    print("The scores are NOT sorted.")

print("Largest Score:", largest_score(scores))