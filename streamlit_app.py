import streamlit as st

st.title("Perguntas pra passar seu tempo kk")

# Usamos session_state para controlar o fluxo das perguntas
if "etapa" not in st.session_state:
    st.session_state.etapa = 1


# ------------------------
# PERGUNTA 1
# ------------------------
if st.session_state.etapa == 1:

    entrada = st.text_input("Digite [E] para Entrar ou [S] para Sair:")

    if st.button("Enviar resposta"):
        if entrada.upper() == "E":
            st.success("Você entrou, parabéns.")
        else:
            st.warning("Você saiu.")

        st.session_state.etapa = 2
        st.rerun()


# ------------------------
# PERGUNTA 2
# ------------------------
elif st.session_state.etapa == 2:

    data = st.text_input("Digite a data que nos conhecemos (dd/mm/aaaa):")

    if st.button("Enviar resposta"):
        if data == "29/09/2023":
            st.success("Boa, acertou!")
        else:
            st.error("Errado!!!")

        st.session_state.etapa = 3
        st.rerun()


# ------------------------
# PERGUNTA 3
# ------------------------
elif st.session_state.etapa == 3:

    bar = st.text_input("Digite o nome do bar que nos conhecemos:")

    if st.button("Enviar resposta"):
        if bar.lower() == "manga rosa".lower():
            st.success("Parabéns!")
        else:
            st.error(":(")

        st.session_state.etapa = 4
        st.rerun()


# ------------------------
# FINAL
# ------------------------
elif st.session_state.etapa == 4:
    st.success("Você terminou todas as perguntas! refaça para passar o tempo KKK TE AMO ")
    if st.button("Recomeçar"):
        st.session_state.etapa = 1
        st.rerun()
