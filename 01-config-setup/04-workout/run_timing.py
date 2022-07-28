
def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        timing = input("Enter 10k run time: ").strip()

        if not timing:
            break

        if not timing.isnumeric():
            continue

        number_of_runs += 1
        total_time += float(timing)

    print(f"Average time of runs is {total_time/number_of_runs}")

run_timing()