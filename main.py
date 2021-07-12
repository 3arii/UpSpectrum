from SignalAnalysis import *

freq_sum = format_data(r"C:\Users\deniz\OneDrive\Documents\Deniz the Laps\Wewalk\Wewalk System Analysis\output.xlsx", "B")
level_sum = format_data(r"C:\Users\deniz\OneDrive\Documents\Deniz the Laps\Wewalk\Wewalk System Analysis\output.xlsx", "C")

broken_freq_sum = format_data(r"C:\Users\deniz\OneDrive\Documents\Deniz the Laps\Wewalk\Wewalk System Analysis\broken_output.xlsx", "B")
broken_level_sum = format_data(r"C:\Users\deniz\OneDrive\Documents\Deniz the Laps\Wewalk\Wewalk System Analysis\broken_output.xlsx", "C")

print(f"The frequencey sum is {freq_sum} while the broken servo sum is {broken_freq_sum}.")
print(f"The level sum is {level_sum} while the broken servo sum is {broken_level_sum}.")