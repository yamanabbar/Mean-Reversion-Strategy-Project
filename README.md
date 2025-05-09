# Mean-Reversion-Strategy-Project
# Mean Reversion Strategy - MSFT vs AAPL

## Overview
This project demonstrates a **mean reversion trading strategy** using historical adjusted closing price data for **Microsoft (MSFT)** and **Apple (AAPL)**. The strategy uses a **Z-score** calculation to determine when to enter and exit positions based on the spread between MSFT and AAPL.

## Strategy Explanation
- **Mean Reversion**: The assumption is that the spread between the two stocks tends to revert to the mean over time.
- **Z-Score**: Measures the deviation of the spread from its mean, helping to decide whether to enter or exit a trade.
- **Positions**:
  - If the Z-score is **high** (above 1 or 2), short MSFT and long AAPL (expecting the spread to narrow).
  - If the Z-score is **low** (below -1 or -2), long MSFT and short AAPL (expecting the spread to widen).

## How to Run the Code
1. Clone the repository:
    ```bash
    git clone https://github.com/yamanabbare/Mean-Reversion-Strategy-Project.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script:
    ```bash
    python mean_reversion_strategy.py
    ```

## Results
- **Total Return**: 19.07%
- **Annualized Return**: 3.43%
- **Annualized Volatility**: 15.54%
- **Sharpe Ratio**: 0.22

## Files
- `mean_reversion_strategy.py`: Python script implementing the backtest.
- `MSFT.CSV`: Historical data for Microsoft.
- `AAPL.csv`: Historical data for Apple.
- `mean_reversion_strategy.xlsx`: Excel file containing the output 
