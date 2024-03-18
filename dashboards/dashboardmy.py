#Projetos iniciais com streamlite 

import streamlit as st 
import time 

def main():
    st.title("Teste de masculinidade")
    st.write("Veremos se você realmente é macho")

    st.header("Definiremos a partir de seu cpf e sua preferencia automobilistica se você nasceu para ser macho!")
    input_text = st.text_input('Digite seu cpf aqui')
    if input_text:
        st.write("Você digitou", input_text)

    st.header('selecione o veiculo do seu sonho')
    selected_option =st.selectbox('Selecione uma opção',[
        'Opção 1: Opala 1968 ', 'Opção 2: Renault Kwid ', 'Opção 3: Byd elétrico'
     ] )
    
    if selected_option:
        st.write ("Opção selecionada", selected_option)


main()

