n_player = 0
for player in self.players:
    n_player += 1
    for info in range(0, 2, 1):
        info_label = ttk.Label(score_frame, text=player[info])
        info_label.grid(column=info, row=n_player)