import streamlit as st

# Função para calcular a probabilidade de vitória e a odd justa
def calcular_probabilidade_vitoria(total_wins, home_wins, h2h_wins, xg_home, xg_away):
    # Transformar % de vitórias em decimais
    total_wins = total_wins / 100
    home_wins = home_wins / 100
    h2h_wins = h2h_wins / 100
    
    # Calcular probabilidade ponderada
    p_vitoria = (total_wins * 0.3) + (home_wins * 0.3) + (h2h_wins * 0.2) + ((xg_home / (xg_home + xg_away)) * 0.2)
    
    # Calcular odd justa
    odd_justa = 1 / p_vitoria if p_vitoria > 0 else float('inf')
    
    # Retornar probabilidade em % e odd justa
    return round(p_vitoria * 100, 2), round(odd_justa, 2)

# Título do app
st.title("Calculadora de Odd Justa")

# Inputs no Streamlit
total_wins = st.number_input("Informe a % de vitórias no total", min_value=0.0, max_value=100.0, value=60.0, step=0.1)
home_wins = st.number_input("Informe a % de vitórias em casa", min_value=0.0, max_value=100.0, value=70.0, step=0.1)
h2h_wins = st.number_input("Informe a % de vitórias no H2H", min_value=0.0, max_value=100.0, value=50.0, step=0.1)
xg_home = st.number_input("Informe o xG do time da casa", min_value=0.0, value=1.8, step=0.1)
xg_away = st.number_input("Informe o xG do time visitante", min_value=0.0, value=1.2, step=0.1)

# Botão para calcular
if st.button("Calcular"):
    probabilidade, odd_justa = calcular_probabilidade_vitoria(total_wins, home_wins, h2h_wins, xg_home, xg_away)
    
    # Exibir os resultados
    st.subheader("Resultados")
    st.write(f"Probabilidade de vitória: **{probabilidade}%**")
    st.write(f"Odd justa: **{odd_justa}**")
