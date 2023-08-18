import tkinter as tk
import boto3

root=tk.Tk()
root.geometry("400x240")
root.title("Sentimental Analysis for text analytics")
textExample=tk.Text(root,height=10)
textExample.pack()
def getText():
    aws_mag_con=boto3.session.Session(profile_name="demo_user")
    client=aws_mag_con.client(service_name='comprehend',region_name="us-east-1")
    result=textExample.get("1.0","end")
    print(result)
    response=client.detect_sentiment(Text=result,LanguageCode='en')
    print(response)
btnRead=tk.Button(root,height=1,width=10,text="Read",command=getText)
btnRead.pack()
root.mainloop()

