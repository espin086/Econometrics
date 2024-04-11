import argparse
import pandas as pd

import statsmodels.api as sm


def run_diff_in_diff(data, treatment, post, outcome_variable, confounding_variables):
    """compute difference-in-differences estimate"""
    data["treatment_post"] = data[treatment] * data[post]

    X = data[[treatment, post, "treatment_post"] + confounding_variables]
    X = sm.add_constant(X)

    model = sm.OLS(data[outcome_variable], X).fit()
    return model.summary()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run difference-in-differences analysis"
    )
    parser.add_argument("data_file", type=str, help="Path to the data file")
    parser.add_argument("treatment", type=str, help="Treatment variable")
    parser.add_argument("post", type=str, help="Post variable")
    parser.add_argument("outcome_variable", type=str, help="Outcome variable")
    parser.add_argument(
        "confounding_variables", nargs="*", help="List of confounding variables"
    )

    args = parser.parse_args()

    data = pd.read_excel(args.data_file)  # Assuming data is in Excel format

    result = run_diff_in_diff(
        data,
        args.treatment,
        args.post,
        args.outcome_variable,
        args.confounding_variables,
    )
    print(result)
