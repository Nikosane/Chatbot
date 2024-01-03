import tkinter as tk
import pypyodbc as odbc
import datetime
from tkinter import PhotoImage
from PIL import Image, ImageTk
import customtkinter 
from tkinter import END
import random
import json
from prompt_data_base import conn 
from chatbot import bot_name , get_response 


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("University ChatBot")
        self.geometry('710x510')
        self.resizable(False, False)
        self.wm_attributes('-transparentcolor','red')

        

        self.frame1 = tk.Frame(self,bg='#343541')
        self.frame1.place(relwidth=1, relheight=1)

        self.background_image_path = 'D:\website\gradient.png'
        self.background_image = PhotoImage(file=self.background_image_path)
        self.background_label = tk.Label(master = self.frame1, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        # frame
        self.frame = customtkinter.CTkFrame(self, height=600,
                                             width=220,
                                             corner_radius=8,
                                             border_width=2,
                                             fg_color="black",
                                             bg_color="black",
                                             border_color="#9764CB")
        self.frame.pack(fill="y", side="left", padx=8, pady=5)

        self.second_frame = customtkinter.CTkFrame(master=self.frame,
                                                    corner_radius=8,
                                                    border_width=2,
                                                    height=100,
                                                    width=150)
        self.second_frame.pack(padx=8, pady=8)

        # image(slrtd logo)
        self.image_path = "D:\website\slrtdc_logo.png"
        self.img1 = PhotoImage(file=self.image_path,format="png")
        self.img_label = tk.Label(master=self.second_frame, image=self.img1,bg="black")
        self.img_label.pack()

        self.image2_path = 'D:\ChatBot\image.png'
        self.img2 = PhotoImage(file=self.image2_path, format="png") 
        self.img_label2 = tk.Label(self, image=self.img2,bg="black")
        self.img_label2.place(x=220,y=1)

        
        # self.uni = "D:\website\UNI.png"
        # self.img6 = PhotoImage(file=self.uni, format="png") 
        # self.img_label6 = tk.Label(master=self.frame, image=self.img6,bg="black")
        # self.img_label6.place(x = 10, y = 200)


        self.image3_path = "D:\website\pngegg.png"
        self.img3 = PhotoImage(file=self.image3_path, format="png") 
        self.img_label3 = tk.Label(master=self.frame, image=self.img3,bg="black")
        # self.img_label3.place(x=5, y=400)
        self.img_label3.place(x=5, y=400)

        


        # text box
        self.text_box = customtkinter.CTkTextbox(self, height=400,
                                                 width=400,
                                                 corner_radius=8,
                                                 fg_color="#222222",
                                                 border_width=1,
                                                 bg_color="black",
                                                 wrap="word",
                                                 border_color="grey")
        self.text_box.place(x=150, y=50)
        text = "How can i help you ?"
        self.text_box.insert(END , text )
        self.text_box.configure(cursor="arrow", state="disabled")
        

        # entry box
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter your Query",
                                            corner_radius=8,
                                            height=50,
                                            fg_color="#222222",
                                            width=280,
        
                                            border_width=1,
                                            bg_color="black",
                                            border_color="grey")
        self.entry.place(x=150, y=455)
        self.entry.bind("<Return>", self._on_enter_pressed)

        

        # send button
        self.send_button = customtkinter.CTkButton(self,
                                                    text="Send",
                                                    height=40, width=100,
                                                    fg_color="#7d2cd4",
                                                    corner_radius=8,
                                                    border_width=2,
                                                    bg_color="black",
                                                    command=lambda: self._on_enter_pressed(None)
                                                    )
        self.send_button.place(x=450,y=460)

        self.send_button.bind("<Enter>", self.on_enter)
        self.send_button.bind("<Leave>", self.on_leave)

        self.rectfier = r"D:\website\Brain.png"
        self.img4 = PhotoImage(file=self.rectfier, format="png") 
        self.img4_label = tk.Label(self, image=self.img4,bg="black")
        self.img4_label.place(x = 693, y = 416)

        self.image5_path = r"D:\website\NLP.png"
        self.img5 = PhotoImage(file=self.image5_path, format="png")
        self.img_label5 = tk.Label(self, image=self.img5,bg="black")
        self.img_label5.place(x=860, y=10)

        # self.image7_path = r"D:\website\friends.png"
        # self.img7 = PhotoImage(file=self.image7_path, format="png") 
        # self.img_label7 = tk.Label(self, image=self.img7,bg="black")
        # self.img_label7.place(x=13, y=450)

        self.image6_path = r"D:\website\UNI.png"
        self.img6 = PhotoImage(file=self.image6_path, format="png") 
        self.img_label6 = tk.Label(self, image=self.img6,bg="black")
        self.img_label6.place(x=29, y=200)

    def on_enter(self,event):
        self.send_button.configure(fg_color="#6c14c9") 

    def on_leave(self,event):
        self.send_button.configure(fg_color="#7d2cd4")
        
    def _on_enter_pressed(self, event):
        msg = self.entry.get()
        self.send_button.configure(fg_color="#2b0257")
        self._insert_message(msg, "You")
    

        

        

    def _insert_message(self, msg, sender):
        if not msg:
            return

        bot_reply , probability , tag = get_response(msg)
        user_prompt = msg
        cursor = conn.cursor()
        current_datetime = datetime.datetime.now()
        

        self.entry.delete(0, END)
        msg1 = f"\n{sender} : \n {msg}\n\n"
        self.text_box.configure(state="normal")
        self.text_box.insert(END, msg1)
        self.text_box.configure(state="disabled")


                   
        msg2 = f"{bot_name} : \n{bot_reply}\n--------------------------------------------------------------------------------------------------------------------\n"
        self.text_box.configure(state="normal")
        self.text_box.insert(END, msg2)
        self.text_box.configure(state="disabled")

        def insert_into(msg1 , msg2 , probability , tag):
            try:

                current_datetime = datetime.datetime.now()

                sql_query= f"""
                    INSERT INTO chatbot_prompt (user_prompt, bot_reply , predicted_probability , predicted_tag, Date_Time  )
                    VALUES (?,?,?,?,?)
                """
                cursor.execute(sql_query,(user_prompt , bot_reply , probability , tag, current_datetime ))
                conn.commit()
                print("Data inserted into the database successfully!")
                
            except Exception as e:
                print(f"Error inserting data into the database: {e}")

            finally:
                cursor.close()

        insert_into(msg ,bot_reply,probability, tag) 

        self.text_box.see(END) 


if __name__ == '__main__':
    app = App()
    app.mainloop()
