import sys
import PySimpleGUI as sg
import mysql.connector
con = mysql.connector.connect(host='localhost',database='pontuacao',user='username',password='password',port=3306)

# ---------------------------------------------------------------------------------
tabela="""----------Tabela de Pontuação----------

               Aprensentar ideia : 10 pontos
               Não aplicável : 0 pontos
               Aplicável : 50 pontos

               Melhoria : 100 pontos
               Grande Benefício : 200 pontos
               Médio Benefício : 100 pontos
               Baixo Benefício : 50 pontos
               Retorno Financeiro : até 1000 pontos

               Inovação : 500 pontos
               Grande Benefício : 600 pontos
               Médio Benefício : 300 pontos
               Baixo Benefício : 150 pontos
               Retorno Financeiro : até 3000 pontos
               ------------------------------------"""
layout = [[sg.Text(tabela)],
          [sg.Text('Coloque o Nome')],[sg.Input('', size=(10, 1), key='input1')],
          [sg.Text('Coloque a pontuação')],[sg.Input('', size=(10, 1), key='input2')],
          [sg.Text('Coloque o custo')],[sg.Input('', size=(10, 1), key='input3')],
          [sg.Button('Enviar')]]
window = sg.Window('Pontuação', layout,
                   default_button_element_size=(5, 2),
                   auto_size_buttons=False,
                   grab_anywhere=False)

while True:
    event, values = window.read()  # read the form
    if event == sg.WIN_CLOSED:
        # if the X button clicked, just exit
        break
        exit()
    elif event == 'Enviar':
        keys_entered1 = values['input1']
        keys_entered2 = values['input2']
        keys_entered3 = values['input3']
        query = (
            f"INSERT INTO pontuacao (nome,pontos,custas) VALUES ('{keys_entered1}',{keys_entered2},{keys_entered3})")

        cursor = con.cursor(buffered=True)
        cursor.execute(query)
        con.commit()
        con.close()

        window.close()

