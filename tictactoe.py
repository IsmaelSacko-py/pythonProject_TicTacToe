import customtkinter as ctk
from PIL import Image

class TicTacToe:

    def __init__(self, gui : ctk.CTk):
        self.__gui = gui
        self.__tour=0
        self.__joueur1Score=[ [0,0,0], [0,0,0], [0,0,0] ]
        self.__joueur2Score=[ [0,0,0], [0,0,0], [0,0,0] ]
        self.__scorePlayer1=0
        self.__scorePlayer2=0
        self.__game_buttons = list()
        self.__list_images = list()


    def create_game_interface(self):
        self.__divCont=ctk.CTkFrame(self.__gui, fg_color='white',width=400,height=450, corner_radius=10)
        self.__divCont.pack_propagate(False)
        self.__divCont.pack(expand=1)
        # j1=ctk.CTkLabel(divCont, text="Joueur1", text_color = 'black',font=('Algerian',13,'bold'))
        # j1.grid(row = 0, column =0 )
        # j2=ctk.CTkLabel(divCont, text="Joueur2", text_color = 'black',font=('Algerian',13,'bold'))
        # j2.grid(row = 1, column = 0)



        self.__divTop=ctk.CTkFrame(self.__divCont, fg_color='white',width=480,height=60)
        self.__divTop.pack_propagate(False)
        self.__divTop.pack(pady=(10, 0))

        self.__divTopJoueur1=ctk.CTkFrame(self.__divTop, bg_color = 'white', fg_color='black' , width=150,height=65, corner_radius=10, border_width=3, border_color='white')
        self.__divTopJoueur1.grid_propagate(False)
        self.__divTopJoueur1.grid(row=0, column=0, padx=(0, 80))

        self.__Img1=ctk.CTkImage(Image.open("Images/rond.png"),size=(20,20))
        self.__Img2=ctk.CTkImage(Image.open("Images/croix.png"),size=(20,20))

        self.__libelle_Joueur1=ctk.CTkLabel(self.__divTopJoueur1, text="Joueur1", image = self.__Img1, compound="right",font=('Algerian',13,'bold'))
        self.__libelle_Joueur1.grid(row=0,column=0, padx=(10, 0), pady=(3, 0))

        self.__libelle_Score1=ctk.CTkLabel(self.__divTopJoueur1,text=f"Score: {self.__scorePlayer1}",font=('Algerian',13,'bold'))
        self.__libelle_Score1.grid(row=1,column=0)

        self.__divTopJoueur2=ctk.CTkFrame(self.__divTop,bg_color='white', fg_color = 'black',width=150,height=65, corner_radius=10, border_width=3, border_color='white')
        self.__divTopJoueur2.grid_propagate(False)
        self.__divTopJoueur2.grid(row=0, column=1)

        self.__libelle_Joueur2=ctk.CTkLabel(self.__divTopJoueur2,text="Joueur2", image = self.__Img2, compound="right",font=('Algerian',13,'bold'))
        self.__libelle_Joueur2.grid(row=0, column=0, padx=(10, 0), pady=(3, 0))

        self.__libelle_Score2=ctk.CTkLabel(self.__divTopJoueur2,text=f"Score: {self.__scorePlayer2}",font=('Algerian',13,'bold'))
        self.__libelle_Score2.grid(row=1, column=0)

        

        self.__divJeu=ctk.CTkFrame(self.__divCont,width=300,height=300, fg_color="white")
        self.__divJeu.pack_propagate(False)
        self.__divJeu.pack(expand=1)

        self.__create_game_buttons()


    def __showImage(self, a, b):
        global __tour, __joueur1Score, __joueur2Score
        if self.__joueur1Score[a][b]!=1 and self.__joueur2Score[a][b]!=1:
            print(f"self.__tour ({'joueur 1' if self.__tour%2 ==0 else 'joueur 2'}) = {self.__tour}")

            image_name = "rond" if self.__tour % 2 == 0 else "croix"
            joueur = self.__joueur1Score if self.__tour % 2 == 0 else self.__joueur2Score

            # print(f"self.__tour = {self.__tour}")
            Img1=ctk.CTkImage(Image.open(f"Images/{image_name}.png"),size=(80,80))
            label_img1=ctk.CTkLabel(self.__game_buttons[a][b],image=Img1,text="")
            label_img1.place(x=8,y=12)
            self.__list_images.append(label_img1)
            joueur[a][b]=1

                
            self.__verif_gagnant()
            self.__tour=self.__tour+1

    def __matchNul(self):
        global __list_images, __joueur1Score, __joueur2Score, __tour
        self.__gestion_bouttons(state = 'readonly')
        for image in self.__list_images:
            image.destroy()
        self.__list_images = []
        self.__joueur1Score=[[0,0,0], [0,0,0], [0,0,0]]
        self.__joueur2Score=[[0,0,0], [0,0,0], [0,0,0]]
        self.__tour = 0

    def __nextLevel(self):
        """permet de passer au niveau supérieur"""
        self.__matchNul()
        self.__divTopJoueur1.configure(border_color='white')
        self.__divTopJoueur2.configure(border_color='white')


    def __gestion_bouttons(self, state = 'disabled'):
        for buttons in self.__game_buttons:
            # print(buttons)
            for button in buttons:
                button.configure(state = state)

    def __verif_gagnant(self):
        """permet de vérifier lequel des joueurs à gagner la partie"""
        global __scorePlayer1, __scorePlayer2, __matchNul

        print(f"Valeur de self.__tour = {self.__tour}")
        if(self.__tour%2==0):
            if self.check_rows_and_spans(self.__joueur1Score) or self.__check_diagonals(self.__joueur1Score):
                self.__scorePlayer1=self.__scorePlayer1+1
                self.__libelle_Score1.configure(text=f"Score: {self.__scorePlayer1}")
                self.__divTopJoueur1.configure(border_color='#00FF00')

                self.__gestion_bouttons()
                self.__gui.after(1000, lambda: self.__nextLevel())

            if self.__tour == 8: 
                self.__gui.after(1000, lambda: self.__matchNul())

        else:

            if self.check_rows_and_spans(self.__joueur2Score) or self.__check_diagonals(self.__joueur2Score):
                self.__scorePlayer2=self.__scorePlayer2+1
                self.__libelle_Score2.configure(text=f"Score: {self.__scorePlayer2}")
                self.__divTopJoueur2.configure(border_color='#00FF00')
                # divTopJoueur1.configure(border_color='red')
                print("Le joueur 2 a gagne")
                self.__gestion_bouttons()

                # for buttons in self.__game_buttons:
                #     # print(buttons)
                #     for button in buttons:
                #         button.bind("<Button-1>", lambda event: 'break')
                self.__gui.after(1000, lambda: self.__nextLevel())

        




    def check_rows_and_spans(self, joueur):
        """verifie s'il y a trois '1' alignés su la même ligne ou la même colonne."""

        def Transpose(joueur) -> list:
            return [[joueur[i][j] for i in range(len(joueur))] for j in range(len(joueur[0]))]
        
        print(f'joeur = {joueur}')
        joueurTranspose = Transpose(joueur) if len(joueur) == 3 else joueur
        for score1, score2 in zip(joueur, joueurTranspose):
            if 0 not in score1:
                return True
            if 0 not in score2:
                return True
        return False

    def __check_diagonals(self, joueur1Score):
        """verifie s'il y a trois '1' alignés sur les deux diagonals"""

        diagonales, diagonale_principale, diagonale_secondaire=[], [], []

        for i in range(len(joueur1Score)):
            for j in range(len(joueur1Score)):
                if i == j:
                    diagonale_principale.append(joueur1Score[i][j])
                if i + j == len(joueur1Score)-1:
                    diagonale_secondaire.append(joueur1Score[i][j])
        print(f'diagonale principale = {diagonale_principale}')
        print(f'diagonal secondaire = {diagonale_secondaire}')
        diagonales.append(diagonale_principale)
        diagonales.append(diagonale_secondaire)

        return self.check_rows_and_spans(diagonales)
        
        
    def __create_game_buttons(self):
        global __game_buttons
        #Ligne 1
        self.__boutton0_0=ctk.CTkButton(self.__divJeu,width=100,height=100, state = 'readonly', text="", hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 0, b = 0))
        # self.__boutton0_0.pack_propagate(False)
        self.__boutton0_0.place(x=0,y=0)
        self.__boutton0_0.bind("<Button-1>", lambda event: print('break'))


        self.__boutton0_1=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 0, b = 1))
        self.__boutton0_1.place(x=100,y=0)

        self.__boutton0_2=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 0, b = 2))
        self.__boutton0_2.place(x=200,y=0)

        #Ligne 2

        self.__boutton1_0=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 1, b = 0))
        self.__boutton1_0.place(x=0,y=100)

        self.__boutton1_1=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 1, b = 1))
        self.__boutton1_1.place(x=100,y=100)

        self.__boutton1_2=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 1, b = 2))
        self.__boutton1_2.place(x=200,y=100)

        #Ligne 3

        self.__boutton2_0=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 2, b = 0))
        self.__boutton2_0.place(x=0,y=200)

        self.__boutton2_1=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 2, b = 1))
        self.__boutton2_1.place(x=100,y=200)

        self.__boutton2_2=ctk.CTkButton(self.__divJeu,width=100,height=100, text="", state = 'readonly', hover=False,border_width=2,border_color='white', fg_color='black', command=lambda:self.__showImage(a = 2, b = 2))
        self.__boutton2_2.place(x=200,y=200)


        self.__game_buttons=[
            [self.__boutton0_0,self.__boutton0_1,self.__boutton0_2],
            [self.__boutton1_0,self.__boutton1_1,self.__boutton1_2],
            [self.__boutton2_0,self.__boutton2_1,self.__boutton2_2]
        ]

    # self.__gui.mainloop()

