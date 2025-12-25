import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    counter = {"R": "P", "P": "S", "S": "R"}

    # simpan history kita
    if not hasattr(player, "my_history"):
        player.my_history = []

    # ===============================
    # DETEKSI ABBEY (counter kita)
    # ===============================
    if len(opponent_history) > 4 and len(player.my_history) > 4:
        abbey_hits = 0
        for i in range(1, len(opponent_history)):
            if opponent_history[i] == counter[player.my_history[i-1]]:
                abbey_hits += 1

        # JIKA ABBEY → FULL RANDOM
        if abbey_hits / len(opponent_history) > 0.55:
            move = random.choice(["R", "P", "S"])
            player.my_history.append(move)
            return move

    # ===============================
    # QUINCY (pola tetap)
    # ===============================
    if len(opponent_history) >= 5:
        quincy_pattern = ["R", "R", "P", "P", "S"]
        match = True
        for i in range(5):
            if opponent_history[-5 + i] != quincy_pattern[i]:
                match = False
                break
        if match:
            move = counter[quincy_pattern[len(player.my_history) % 5]]
            player.my_history.append(move)
            return move

    # ===============================
    # KRIS & MRUGESH (pattern + freq)
    # ===============================
    if len(opponent_history) >= 4:
        patterns = {}
        for i in range(len(opponent_history) - 3):
            seq = "".join(opponent_history[i:i+3])
            nxt = opponent_history[i+3]
            if seq not in patterns:
                patterns[seq] = {"R": 0, "P": 0, "S": 0}
            patterns[seq][nxt] += 1

        last = "".join(opponent_history[-3:])
        if last in patterns:
            predicted = max(patterns[last], key=patterns[last].get)
            move = counter[predicted]
            player.my_history.append(move)
            return move

    # ===============================
    # DEFAULT
    # ===============================
    move = random.choice(["R", "P", "S"])
    player.my_history.append(move)
    return move
