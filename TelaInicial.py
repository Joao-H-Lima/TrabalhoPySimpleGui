# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 21:36:55 2023

@author: android
"""

import PySimpleGUI as sg

sg.theme("LightGrey1")

pessoas_cadastradas = list() #aonde guardar pessoas


def dict_para_matriz():
    matriz_de_registros=list()
    for contador in range(len(pessoas_cadastradas)):
        registro = list()
        
        registro.insert(0, contador) 
        registro.insert(1 , pessoas_cadastradas[contador]["CPF"])
        registro.insert(2, pessoas_cadastradas[contador]["Nome"])
        registro.insert(3,  pessoas_cadastradas[contador]["Endereco"])
        registro.insert(4, pessoas_cadastradas[contador]["Cidade"])
        registro.insert(5, pessoas_cadastradas[contador]["Estado"])
        
        if pessoas_cadastradas[contador]["-RADIO_FEMININO-"]:
            registro.insert(6,  "Feminino")
        else:
            registro.insert(6, "Masculino")
        
        registro.insert(7, pessoas_cadastradas[contador]["E-mail"])
        registro.insert(8, pessoas_cadastradas[contador]["Data Nascimento"])
        registro.insert(9, pessoas_cadastradas[contador]["Obs"])
        
        matriz_de_registros.append(registro)
    return matriz_de_registros

#Mostra tela cadastrar
def cadastrar():
    layout_radio = [
                    [sg.Radio('Feminino', group_id = 'radio_sexo', key = '-RADIO_FEMININO-'), 
                     sg.Radio('Masculino', group_id = 'radio_sexo', key = '-RADIO_MASCULINO-')]
            ]
    estados = ['AC', 'AL', 'AP', 'AM', 
               'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
               'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
               'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']    

    layout_cadastro = [
        [sg.Text('CADASTRO DE PESSOAS', size=(60,1), justification='center')],

        [sg.Text('CPF:', size = (4, 1)),sg.Input(key = 'CPF',size = (13, 1)),sg.Text('Nome:',size = (7, 1)),sg.Input(key = 'Nome',size = (38, 1))],

        [sg.Text('Endereço'),sg.Input(key = 'Endereco',size = (60, 1))],

        [sg.Text('Cidade:',size = (7,1)),sg.Input(key = 'Cidade',size = (30,1)),
         
         sg.Text('Estado:', size = (6,1)),sg.Combo(values = estados, k = 'Estado', size = (17,1))],

        [ sg.Frame('Sexo', layout_radio)], 

        [
            sg.Text('E-mail:',size = (7,1)),sg.Input(key = 'E-mail',size = (30,1)),
            sg.Text('Data Nascimento:',size = (14,1)),sg.Input(key = 'Data Nascimento',size = (10,1))
         ],

        [
            sg.Text('Observações: ',size = (10,1)), sg.Multiline(enable_events=True, key = 'Obs',expand_x=True, expand_y=True, size=(0,5), justification='left')
        ],

        [
            sg.Push(), sg.Button('Cadastrar', size=(10, 2)), sg.Push()]
        ]
    
    window = sg.Window('Tela de Cadastro', layout_cadastro)

    while True:

        event, values = window.read()

        if event == 'Cadastrar':
          sg.popup('Cadastro Realizado com Sucesso!!!')
          pessoas_cadastradas.append(values)
          window['CPF'].update('')
          window['Nome'].update('')
          window['Endereco'].update('')
          window['Cidade'].update('')
          window['Estado'].update('')
          window['-RADIO_FEMININO-'].update(False)
          window['-RADIO_MASCULINO-'].update(False)
          window['E-mail'].update('')
          window['Data Nascimento'].update('')
          window['Obs'].update('')

        #se fechar janela voltar para função principal
        if event == sg.WIN_CLOSED:
            return None

#mostra tela editar
def editar():
    toprow= ['ID', 'CPF', 'NOME', 'ENDEREÇO', 'CIDADE', 'ESTADO', 'SEXO', 'E-MAIL', 'DATA DE NASCIMENTO', 'OBSERVAÇÕES']
    registros = dict_para_matriz()
    layout_editar = [
                        [
                            sg.Push(),
                            sg.Text('PESSOAS CADASTRADAS'),
                            sg.Push()
                        ],
                        
                        [
                         sg.Table(values= registros,headings=toprow, auto_size_columns=True,display_row_numbers=False, justification='center',  expand_x=True, expand_y=True, enable_click_events=True, key = 'list')
                        ],
                        
                        [
                            sg.Push(),
                            sg.Button('Remover', size=(10, 2)),
                            sg.Push()
                        ]
                    ]  

    window = sg.Window('Lista das Pessoas Cadastradas', layout_editar)

    while True:

        event, values = window.read() 
        
        if event == 'Remover':
            selected_row = values['list'][0]
            pessoas_cadastradas.pop(selected_row)
            registros = dict_para_matriz()  # Atualiza a lista de registros
            window['list'].update(registros)



        if event == sg.WIN_CLOSED:
           return None
   

#mostra tela sobre
def sobre():
    layout = [[sg.Listbox(['Nome:João Henrique', 
                           'Formações: Engenharia de Software', 
                           'Cargo: Estudantes',
                           'Instituiçaõ de Ensino: UNIFAE- São João da Boa Vista'], size=(40, 4), expand_y=True, disabled=True),]] 

    window = sg.Window('Informações sobre os Autores', layout)

    while True:

        event, values = window.read() 

        if event == sg.WIN_CLOSED:
            return None
#mostra tela menu
def menu():
    opcoes = [
                ['Pessoa',['Cadastrar','Editar']],
                ['Ajuda',['Sobre']]
            ]

    layout =[
            [sg.Menu(opcoes)],[sg.Image('imagem.png')]]
    
    window = sg.Window('Tela de Menu', layout)
    
    while True:
        event, values = window.read()
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        if event == 'Sobre':
            sobre()
        
        elif event == 'Cadastrar':
            window.hide()#esconder janela
            cadastrar()
        elif event == 'Editar':
            window.hide()
            editar()
            
        window.un_hide()#mostrar janela novamente

#função principal
def main():
    menu()

main()
