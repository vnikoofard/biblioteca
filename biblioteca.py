import streamlit as st
import pandas as pd

# criar titulo do aplicativo
st.title("Biblioteca de Livros")

livros = pd.DataFrame(columns=['ISBN', 'titulo', 'autor', 'ano_publicacao', 'genero'])
estudantes = pd.DataFrame(columns=['matricula', 'nome', 'curso', 'telefone', 'email'])
emprestimos = pd.DataFrame(columns=['id_emprestimo', 'matricula_estudante', 'ISBN_livro', \
                                    'data_emprestimo', 'data_devolucao'])
# adicionar alguns livros ao dataframe livros
novos_livros = pd.DataFrame([
    {'ISBN': '978-3-16-148410-0', 'titulo': 'Livro A', 'autor': 'Autor A', 'ano_publicacao': 2020, 'genero': 'Ficção'},
    {'ISBN': '978-1-23-456789-7', 'titulo': 'Livro B', 'autor': 'Autor B', 'ano_publicacao': 2018, 'genero': 'Romance'}
])
livros = pd.concat([livros, novos_livros], ignore_index=True)

# adicionar alguns estudantes ao dataframe estudantes
novos_estudantes = pd.DataFrame([
    {'matricula': '2023001', 'nome': 'João Silva', 'curso': 'Engenharia', 'telefone': '123456789', 'email': 'joao.silva@email.com'},
    {'matricula': '2023002', 'nome': 'Maria Souza', 'curso': 'Medicina', 'telefone': '987654321', 'email': 'maria.souza@email.com'}
])
estudantes = pd.concat([estudantes, novos_estudantes], ignore_index=True)

# adicionar um livro emprestado ao dataframe emprestimos
novo_emprestimo = pd.DataFrame([
    {'id_emprestimo': 1, 'matricula_estudante': '2023001', 'ISBN_livro': '978-3-16-148410-0', 'data_emprestimo': '2024-06-01', 'data_devolucao': '2024-06-15'}
])
emprestimos = pd.concat([emprestimos, novo_emprestimo], ignore_index=True)

# quero ter um sidebar com as opções de menu para o usuário escolher entre "Livros", "Estudantes" e "Empréstimos"
menu = st.sidebar.selectbox("Selecione uma opção", ["Livros", "Estudantes", "Empréstimos"])
if menu == "Livros":
    st.subheader("Lista de Livros")
    st.dataframe(livros)
elif menu == "Estudantes":
    st.subheader("Lista de Estudantes")
    st.dataframe(estudantes)
elif menu == "Empréstimos":
    st.subheader("Lista de Empréstimos")
    st.dataframe(emprestimos)