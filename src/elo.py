def update_elo(elo_a, elo_b, score_a, k=20):
    expected_a = 1 / (1 + 10 ** ((elo_b - elo_a) / 400))
    actual_a = score_a

    new_elo_a = elo_a + k * (actual_a - expected_a)
    new_elo_b = elo_b + k * ((1 - actual_a) - (1 - expected_a))

    return new_elo_a, new_elo_b
