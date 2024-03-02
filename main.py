import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
from PIL import Image, ImageTk
import webbrowser

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Little Noseptimizer")
        self.root.geometry("600x400")
        
        # Definindo o ícone do aplicativo
        icon_path = os.path.join(os.path.dirname(__file__), "icons", "app_icon.png")
        self.root.iconphoto(True, tk.PhotoImage(file=icon_path))
        
        self.tab_control = ttk.Notebook(root)
        
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.tab1, text="Opções")
        self.tab_control.add(self.tab2, text="Sobre")
        
        self.tab_control.pack(expand=1, fill="both", padx=10, pady=10)
        
        self.create_widgets_tab1()
        self.create_widgets_tab2()
        
        self.create_footer_buttons()
    
    def create_widgets_tab1(self):
        self.tab1_frame = tk.Frame(self.tab1, bg="lightgray")
        self.tab1_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        self.button1 = tk.Button(self.tab1_frame, text="Limpar Temp", command=self.clear_temp, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
        self.button1.pack(pady=5)
        self.set_button_icon(self.button1, "folder_icon.png")
        
        self.button2 = tk.Button(self.tab1_frame, text="Exibir Créditos", command=self.show_credits, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
        self.button2.pack(pady=5)
        self.set_button_icon(self.button2, "credits_icon.png")
        
        self.button3 = tk.Button(self.tab1_frame, text="Deletar Arquivos", command=self.delete_files, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
        self.button3.pack(pady=5)
        self.set_button_icon(self.button3, "delete_icon.png")
        
        self.button4 = tk.Button(self.tab1_frame, text="Fechar App", command=self.root.quit, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
        self.button4.pack(pady=5)
        self.set_button_icon(self.button4, "close_icon.png")
        
    def create_widgets_tab2(self):
        self.tab2_frame = tk.Frame(self.tab2, bg="lightgray")
        self.tab2_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        about_text = "Little Noseptimizer\nVersão 1.0\nDesenvolvido por littlenose (pyetrodev)\nContato: delabelapyetro77@gmail.com"
        self.label_about = tk.Label(self.tab2_frame, text=about_text, bg="lightgray", font=("Arial", 12))
        self.label_about.pack(pady=10)
    
    def create_footer_buttons(self):
        self.footer_frame = tk.Frame(self.root, bg="lightgray")
        self.footer_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)
        
        self.discord_button = tk.Button(self.footer_frame, text="Discord", command=self.open_discord, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
        self.discord_button.pack(side=tk.RIGHT, padx=10)
        self.set_button_icon(self.discord_button, "discord_icon.png")
        
        self.youtube_button = tk.Button(self.footer_frame, text="YouTube", command=self.open_youtube, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
        self.youtube_button.pack(side=tk.RIGHT)
        self.set_button_icon(self.youtube_button, "youtube_icon.png")
        
        self.footer_label = tk.Label(self.footer_frame, text="Todos os direitos reservados", font=("Arial", 10), bg="lightgray")
        self.footer_label.pack(pady=5)
        
    def set_button_icon(self, button, icon_filename):
        icon_path = os.path.join(os.path.dirname(__file__), "icons", icon_filename)
        icon = Image.open(icon_path)
        icon = icon.resize((20, 20), Image.BILINEAR)
        icon = ImageTk.PhotoImage(icon)
        button.config(image=icon, padx=5, pady=5)
        button.image = icon
    
    def clear_temp(self):
        try:
            temp_folder = os.environ.get('TEMP')
            if temp_folder:
                # Exclui todos os arquivos dentro da pasta Temp
                for filename in os.listdir(temp_folder):
                    file_path = os.path.join(temp_folder, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print("Erro ao excluir o arquivo {}: {}".format(file_path, e))
                print("Pasta Temp limpa com sucesso!")
            else:
                print("Não foi possível encontrar a pasta Temp.")
        except PermissionError:
            print("Você não tem permissão para excluir arquivos na pasta Temp.")
        except Exception as e:
            print("Erro ao limpar a pasta Temp:", e)
    
    def show_credits(self):
        credits_text = "Desenvolvido por littlenose (pyetrodev)\nContato: delabelapyetro77@gmail.com"
        messagebox.showinfo("Créditos", credits_text)
    
    def delete_files(self):
        selected_folder = filedialog.askdirectory()
        if selected_folder:
            try:
                shutil.rmtree(selected_folder)
                print("Arquivos deletados com sucesso!")
            except Exception as e:
                print("Erro ao deletar os arquivos:", e)
    
    def open_discord(self):
        webbrowser.open("https://discord.gg/HbYnezQaY3")
    
    def open_youtube(self):
        webbrowser.open("https://youtube.com/channel/@Pyetrokkj")

# Adicione este método à classe MyApp para abrir o link do GitHub
def open_github(self):
    webbrowser.open("https://github.com/seu-usuario/seu-repositorio")

# Adicione este widget ao método create_footer_buttons para criar o botão "Source Code"
    self.github_button = tk.Button(self.footer_frame, text="Source Code", command=self.open_github, compound=tk.LEFT, font=("Arial", 12), bd=2, relief="raised")
    self.github_button.pack(side=tk.LEFT, padx=10)
    self.set_button_icon(self.github_button, "github_icon.png")




root = tk.Tk()
app = MyApp(root)
root.mainloop()
