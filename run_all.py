import preprocess
import solve
import postprocess
import argparse
import pulp

def run_all():
    problem, data_to_compute = preprocess.main(level)
    solve.main(data_to_compute)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select Level.")
    parser.add_argument("--level", default="easy", help="select level (easy, medium, hard, user)")
    args = parser.parse_args()
    level = args.level

    problem, data_to_compute = preprocess.main(level)
    status, result = solve.main(data_to_compute)

    print("Problem to solve")

    postprocess.display_data(problem)
    print(" ", "Result", sep="\n")
    postprocess.display_data(result)
    # Print Optimality
    print("Status: ", pulp.LpStatus[status])