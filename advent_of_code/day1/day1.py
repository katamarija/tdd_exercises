input_file = open("day1_input.txt", "r")
content = input_file.readlines()
numbers = []

for line in content:
    number = int(line.strip("\n"))
    numbers.append(number)

def summed_pair(numbers, sum_desired):
    results = {}
    result2 = {}
    for i, e in enumerate(numbers):
        results[e] = i
        result2[i] = e
        key1 = 0
        key2 = 0
        if sum_desired - e in results:
            key1 = results.get(sum_desired-e)
            k1 = result2[key1]
            k2 = result2[i]
            print("pair at key", results.get(sum_desired-e), "and key", i)
            return k1 * k2

print(summed_pair(numbers, 2020))

def summed_triple(numbers, length, sum_desired):
    numbers.sort()
    for i in range(0,length-2):
        first = i + 1
        end = length - 1
        while(first < end):
            if numbers[i] + numbers[first] + numbers[end] == sum_desired:
                print("Triple is", numbers[i], numbers[first], numbers[end])
                return True
            elif numbers[i] + numbers[first] + numbers[end] < sum_desired:
                first += 1
            else:
                end -= 1
        return False

print(summed_triple(numbers, len(numbers), 2020))


def sum_triple(numbers, length, sum_desired):
    numbers.sort()
    for i in range(0,length-1):
        s = set()
        print(s)
        curr_sum = sum_desired - numbers[i]
        for j in range(i + 1, length):
            if curr_sum - numbers[j] in s:
                print("trip",

        first = i + 1
        end = length - 1
        while(first < end):
            if numbers[i] + numbers[first] + numbers[end] == sum_desired:
