# backtesting

## Goals of this project
- develop optimally efficient mechanism for backtesting asset strategies
- MVP
  - mechanism to take an arbitrary asset and backtest a given strategy (given that it is on some supported API we are going to fetch data from) 
    - impl using both Pandas + Polars so we can compare exe time
    - obv accum results + optional audit log
  - mechanism to show execution time
    - for avg strat analysis
    - for cumulative backtesting evaluation time
- Future Expansion
  - Believe that this task will be very well suited to native Pandas/Polars lib calls that will permit vectorized ops, but maybe just for fun impl optimized C++ logic to see if we can get even greater speedup