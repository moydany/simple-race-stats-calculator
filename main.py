"""
You are the designated 'technology specialist' of a local Sporting Organization
(S.O.). Numerous teams of athletes participate in races organized by the
association. Each time, you receive a string containing the race results for
all participating teams. Here's an example string representing the individual
results of a team of 5 runners:

'01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17'

In this format, each part of the string represents the time taken by a runner
in the format 'h|m|s', where 'h' represents hours, 'm' represents minutes,
and 's' represents seconds. Each result is separated by a comma or a comma
followed by a space.

To evaluate and compare the performance of the teams, you need to calculate
three statistics: range, average, and median.

Range: The range is the difference between the lowest and highest values in a
set of numbers. For example, given the set {4, 6, 9, 3, 7},
the lowest value is 3 and the highest value is 9.
Therefore, the range is calculated as 9 - 3 = 6.

Average: The average, also known as the mean, is obtained by adding up all the
numbers in a set and dividing the sum by the total count of numbers.

Median: The median is the middle number that separates the higher half from the
lower half of a data sample. If the sample size is odd, the median is the
middle value. If the sample size is even, the median is the mean of the two
middle values.

Your task is to calculate these three values and return a string in the
following format:

'Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss'

where 'hh', 'mm', and 'ss' represent two-digit integers
(represented as strings).

Please note:

If a result in seconds has decimals (e.g., ab.xy...), it should be truncated to
'ab'. If the given string is empty, your function should return an empty string
as well.

# Test cases
test_1 = stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")

assert test_1 == "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34", \
    "❌ Test 1 failed!"
print("✅ Test 1 passed!")

test_2 = stat(
    "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")

assert test_2 == "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00", \
    "❌ Test 2 failed!"
print("✅ Test 2 passed!")

test_3 = stat("")

assert test_3 == "", "❌ Test 3 failed!"
print("✅ Test 3 passed!")
"""
from utils import convert_to_hms


def stat(s):
    if not s:
        return ""

    times = s.split(", ")
    times_in_seconds = []
    for time in times:
        h, m, s = map(int, time.split("|"))
        total_seconds = h * 3600 + m * 60 + s
        times_in_seconds.append(total_seconds)

    times_in_seconds.sort()

    range_time = max(times_in_seconds) - min(times_in_seconds)
    average_time = sum(times_in_seconds) // len(times_in_seconds)
    if len(times_in_seconds) % 2 == 0:
        median_time = (times_in_seconds[len(
            times_in_seconds) // 2 - 1] + times_in_seconds[len(times_in_seconds) // 2]) // 2
    else:
        median_time = times_in_seconds[len(times_in_seconds) // 2]

    return f'Range: {convert_to_hms(range_time)} Average: {convert_to_hms(average_time)} Median: {convert_to_hms(median_time)}'


def init():
    s = input("Enter the race times (in format 'hh|mm|ss'), separated by commas: ")
    print(stat(s))


if __name__ == "__main__":
    init()
