import streamlit as st
import random

st.set_page_config(
    page_title="Jahnavi's Rock Paper Scissors Game",
    page_icon="🎮",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #4B0082;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

.result {
    padding: 25px;
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    text-align: center;
    margin-top: 25px;
}

.score {
    padding: 15px;
    border-radius: 15px;
    background: white;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎮 Jahnavi\'s Rock Paper Scissors Game</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your move and play against the computer! 🤖</div>',
    unsafe_allow_html=True
)

if "player_score" not in st.session_state:
    st.session_state.player_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "draws" not in st.session_state:
    st.session_state.draws = 0

choices = {
    "🪨 Rock": "Rock",
    "📄 Paper": "Paper",
    "✂️ Scissors": "Scissors"
}

st.subheader("🎯 Choose your move")

player_choice_display = st.radio(
    "Select one:",
    list(choices.keys()),
    horizontal=True
)

if st.button("🎮 Play Game"):

    player_choice = choices[player_choice_display]

    computer_choice = random.choice(
        ["Rock", "Paper", "Scissors"]
    )

    if player_choice == computer_choice:
        result = "🤝 It's a Draw!"
        st.session_state.draws += 1

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "🎉 You Win!"
        st.session_state.player_score += 1

    else:
        result = "🤖 Computer Wins!"
        st.session_state.computer_score += 1

    st.markdown(
        f"""
        <div class="result">
            <h2>{result}</h2>
            <h3>🙋 Your Choice: {player_choice}</h3>
            <h3>🤖 Computer Choice: {computer_choice}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

st.subheader("🏆 Score Board")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="score">
            <h3>🙋 You</h3>
            <h2>{st.session_state.player_score}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="score">
            <h3>🤝 Draws</h3>
            <h2>{st.session_state.draws}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="score">
            <h3>🤖 Computer</h3>
            <h2>{st.session_state.computer_score}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

if st.button("🔄 Reset Game"):
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.draws = 0
    st.rerun()

st.markdown(
    """
    <div style="text-align:center; margin-top:30px; color:#666;">
        🎮 Jahnavi's Rock Paper Scissors Game | Built with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)