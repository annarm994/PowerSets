import itertools

def generate_power_set(input_set):
    power_set = []
    for i in range(len(input_set) + 1):
        power_set.extend(itertools.combinations(input_set, i))
    return power_set

def main():
    user_input = input("Enter Set of Elements Separated by Spaces: ").split()
    power_set = generate_power_set(user_input)
    print("Power Set:")
    for subset in power_set:
        print(subset)

if __name__ == "__main__":
    main()