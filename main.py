from tictactoe import *


gui = ctk.CTk()
gui.geometry("450x450")
gui.title("TIC-TAC-TOE")
gui.resizable(False,False)

tictactoe = TicTacToe(gui)
tictactoe.create_game_interface()

gui.mainloop()