import read
import solve

(capacity, items) = read.read_problem("data/ks_500_0")
solution = solve.solve_knap_sack(capacity, items)
