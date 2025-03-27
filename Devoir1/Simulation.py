import random
import tkinter as tk
from tkinter import messagebox

# Définition de la grille
grid = [
    [0, 0, 0, 0, 0],
    [0, -10, 0, -10, 0],
    [0, 0, 0, 0, 10],  # 10 représente le trésor
]

# Dimensions de la grille
rows = len(grid)
cols = len(grid[0])

# Position de départ
agent_position = [0, 0]

# Déplacements possibles
actions = {'HAUT': (-1, 0), 'BAS': (1, 0), 'GAUCHE': (0, -1), 'DROITE': (0, 1)}

# Variables globales
score = 0
steps = 0
game_running = False

# Création de l'interface Tkinter
root = tk.Tk()
root.title("Agent Intelligent")
canvas = tk.Canvas(root, width=cols*50, height=rows*50)
canvas.pack()

# Labels pour afficher le score et les étapes
score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack()
steps_label = tk.Label(root, text="Étapes: 0", font=("Arial", 12))
steps_label.pack()

# Zone de texte pour l'historique
txt_history = tk.Text(root, height=10, width=50)
txt_history.pack()

# Bouton pour démarrer/redémarrer le jeu
btn_start = tk.Button(root, text="Démarrer", command=lambda: start_game())
btn_start.pack()

def draw_grid():
    """Dessine la grille avec les pièges, le trésor et l'agent."""
    canvas.delete("all")
    for i in range(rows):
        for j in range(cols):
            color = "white"
            if grid[i][j] == -10:
                color = "red"
            elif grid[i][j] == 10:
                color = "gold"
            canvas.create_rectangle(j*50, i*50, (j+1)*50, (i+1)*50, fill=color, outline="black")
    draw_agent()

def draw_agent():
    """Dessine l'agent à sa position actuelle."""
    x, y = agent_position
    canvas.create_oval(y*50+10, x*50+10, y*50+40, x*50+40, fill="blue")

def is_valid_move(pos, move):
    """Vérifie si un déplacement est valide."""
    new_x = pos[0] + move[0]
    new_y = pos[1] + move[1]
    return 0 <= new_x < rows and 0 <= new_y < cols

def start_game():
    """Démarre ou redémarre le jeu."""
    global agent_position, score, steps, game_running
    agent_position = [0, 0]
    score = 0
    steps = 0
    game_running = True
    btn_start.config(state=tk.DISABLED)
    txt_history.delete(1.0, tk.END)
    move_agent()

def move_agent():
    """Déplace l'agent de manière aléatoire et met à jour l'interface."""
    global agent_position, score, steps, game_running

    if not game_running:
        return

    steps += 1
    possible_moves = [move for move in actions.values() if is_valid_move(agent_position, move)]
    move = random.choice(possible_moves)

    # Mise à jour de la position de l'agent
    agent_position[0] += move[0]
    agent_position[1] += move[1]

    # Mise à jour du score et des étapes
    score -= 1
    score_label.config(text=f"Score: {score}")
    steps_label.config(text=f"Étapes: {steps}")

    # Dessiner la grille et l'agent
    draw_grid()
    root.update()

    # Ajouter l'historique
    txt_history.insert(tk.END, f"Étape {steps}: Position {agent_position}, Score {score}\n")
    txt_history.see(tk.END)

    # Vérifier si l'agent a atteint un piège ou le trésor
    cell_value = grid[agent_position[0]][agent_position[1]]
    if cell_value == -10:
        txt_history.insert(tk.END, f"Échec: Piège en {steps} étapes ! Recommençons...\n")
        txt_history.see(tk.END)
        game_running = False
        root.after(1000, reset_game)  # Redémarrer après 1 seconde
    elif cell_value == 10:
        txt_history.insert(tk.END, f"Succès: Trésor trouvé en {steps} étapes avec un score de {score}\n")
        txt_history.see(tk.END)
        game_running = False
        messagebox.showinfo("Succès", f"L'agent a trouvé le trésor en {steps} étapes avec un score de {score} !")
        btn_start.config(state=tk.NORMAL)
    else:
        # Continuer le jeu après un délai
        root.after(500, move_agent)

def reset_game():
    """Réinitialise le jeu après un échec."""
    global agent_position, score, steps, game_running
    agent_position = [0, 0]
    score = 0
    steps = 0
    game_running = True
    move_agent()

# Initialisation de l'interface
draw_grid()
root.mainloop()