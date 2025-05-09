# Mean Reversion Strategy – MSFT vs AAPL

This project implements a **mean reversion trading strategy** using historical adjusted closing price data for **Microsoft (MSFT)** and **Apple (AAPL)**. The strategy identifies long/short trading opportunities based on the **Z-score of the price spread** between the two stocks.

---

## 📈 Strategy Logic

- **Mean Reversion**: Assumes the price spread between MSFT and AAPL reverts to its historical mean.
- **Z-Score**: Measures how far the spread deviates from the mean in standard deviations.
- **Trading Rules**:
  - Z < -1: Long MSFT, Short AAPL
  - Z > +1: Short MSFT, Long AAPL
  - -1 < Z < +1: Exit all positions

---

## 🗂️ Project Files

- `mean_reversion_strategy.py`: Python script with full implementation.
- `MSFT.CSV`: Adjusted close data for Microsoft.
- `AAPL.csv`: Adjusted close data for Apple.
- `mean_reversion_strategy.xlsx`: Strategy results exported to Excel.
- `requirements.txt`: Required Python packages.

---

## 💻 How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yamanabbar/Mean-Reversion-Strategy-Project.git
   cd Mean-Reversion-Strategy-Project

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the script**:
   ```bash
   python mean_reversion_strategy.py
   ```

## Results
- **Total Return**: 19.07%
- **Annualized Return**: 3.43%
- **Annualized Volatility**: 15.54%
- **Sharpe Ratio**: 0.22

## Tools Used
- Python (Anaconda)
- pandas, numpy, matplotlib
- Spyder IDE
- GitHub for version control
  

## Files
- `mean_reversion_strategy.py`: Python script implementing the backtest.
- `MSFT.CSV`: Historical data for Microsoft.
- `AAPL.csv`: Historical data for Apple.
- `mean_reversion_strategy.xlsx`: Excel file containing the output 

Author
Yaman Abbar

This project is for educational purposes only and does not constitute financial advice.


