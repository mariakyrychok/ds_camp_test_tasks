import numpy as np


T, H = 0, 1
coins_heads_prob = np.array([0.1, 0.2, 0.4, 0.8, 0.9])
experiment_results = [H, H, H, T, H, T, H, H]


def main():
    coins_prob = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # initial probability of each coin being selected
    head_prob = np.dot(coins_heads_prob, coins_prob)  # full probability of H in next experiment
    head_prob_seq = []
    for side in experiment_results:
        # update P(m|H) or P(m|T)==P(m|1-H) with Bayes' theorem
        if side == H:
            coins_prob = (coins_heads_prob * coins_prob) / head_prob
        else:
            coins_prob = ((1 - coins_heads_prob) * coins_prob) / (1 - head_prob)

        head_prob = np.dot(coins_heads_prob, coins_prob)
        head_prob_seq.append(round(head_prob, 2))

    print(head_prob_seq)


if __name__ == '__main__':
    main()
