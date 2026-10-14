# Reusable CI example

This project uses a reusable GitHub Actions workflow to run its Python tests.

- [`../.github/workflows/reusable-python-ci.yml`](../.github/workflows/reusable-python-ci.yml) defines a `workflow_call` workflow. It checks out the repository, sets up the requested Python version, installs `requirements.txt`, and runs `tests/` from the supplied working directory.
- [`../.github/workflows/reusable-ci-demo.yml`](../.github/workflows/reusable-ci-demo.yml) calls that workflow for this project and passes its directory and Python version.

To reuse the CI workflow for another Python project in this repository, add a job like this to a caller workflow:

```yaml
jobs:
  python-ci:
    uses: ./.github/workflows/reusable-python-ci.yml
    with:
      working-directory: path/to/project
      python-version: "3.12"
```

The target directory must contain `requirements.txt` and a `tests/` directory.