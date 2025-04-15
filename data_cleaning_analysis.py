name: Python Script Analysis

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  run_python_analysis:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          pip install pandas matplotlib seaborn numpy

      - name: Run Python script
        run: |
          python data_cleaning_analysis.py

      - name: Commit and push generated files
        run: |
          git config --global user.name "Your GitHub Username"
          git config --global user.email "your-email@example.com"
          git add final_data.csv foreign_workers_plot.png gdp_unemployment_plot.png
          git commit -m "Add generated analysis files"
          git push
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
