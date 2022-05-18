import preprocess
import solve
import argparse
import pulp

def run_all():
    data_to_display, data_to_compute = preprocess.main(level)
    solve.main(data_to_compute)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select Level.")
    parser.add_argument("--level", default="easy", help="select level (easy, medium, hard, user)")
    args = parser.parse_args()
    level = args.level

    data_to_display, data_to_compute = preprocess.main(level)
    result_on_table, status = solve.main(data_to_compute)

    print("Prepared Data", data_to_display, "-----------------------------", sep="\n")
    print(" ", "Result", sep="\n")

    print(result_on_table, "-----------------------------", sep="\n")
    
    # Print Optimality
    print("Status: ", pulp.LpStatus[status])