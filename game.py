import numpy as np
import streamlit as st

st.set_page_config(page_title="Pac-Man Manual Game", layout="centered")

st.title("🟡 Pac-Man Arcade Game")
st.write("Use the directional buttons below to steer Pac-Man through the maze and reach the fruit!")

rows, cols = 10, 10

if "pos" not in st.session_state:
    st.session_state.pos = [0, 0]
    st.session_state.target = [rows - 1, cols - 1]
    st.session_state.walls = {
        (1, 1), (1, 2), (1, 3), (3, 3), (3, 4), (3, 5),
        (5, 1), (5, 2), (6, 2), (7, 2), (2, 7), (3, 7), (4, 7)
    }
    st.session_state.score = 0
    st.session_state.won = False

col1, col2 = st.sidebar.columns(2)
if col1.button("Reset Game"):
    st.session_state.pos = [0, 0]
    st.session_state.target = [rows - 1, cols - 1]
    st.session_state.won = False
    st.rerun()

def move(dr, dc):
    if st.session_state.won:
        return
    nr = st.session_state.pos[0] + dr
    nc = st.session_state.pos[1] + dc
    
    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in st.session_state.walls:
        st.session_state.pos = [nr, nc]
        if st.session_state.pos == st.session_state.target:
            st.session_state.won = True

st.write("### Controls")
c1, c2, c3 = st.columns([1, 1, 1])
with c2:
    if st.button("⬆️ Up"):
        move(-1, 0)
        st.rerun()

c4, c5, c6 = st.columns([1, 1, 1])
with c4:
    if st.button("⬅️ Left"):
        move(0, -1)
        st.rerun()
with c6:
    if st.button("➡️ Right"):
        move(0, 1)
        st.rerun()

c7, c8, c9 = st.columns([1, 1, 1])
with c8:
    if st.button("⬇️ Down"):
        move(1, 0)
        st.rerun()

if st.session_state.won:
    st.success("🎉 Waka Waka! You ate the fruit and won the game!")

grid_data = []
for r in range(rows):
    row_chars = []
    for c in range(cols):
        if [r, c] == st.session_state.pos:
            row_chars.append("🟡")
        elif [r, c] == st.session_state.target:
            row_chars.append("🍒")
        elif (r, c) in st.session_state.walls:
            row_chars.append("🧱")
        else:
            row_chars.append("·")
    grid_data.append(row_chars)

import pandas as pd
df = pd.DataFrame(grid_data)

def style_game(val):
    if val == "🧱":
        return 'background-color: #1a1a40; font-size: 24px; text-align: center;'
    elif val == "🟡":
        return 'background-color: #000000; font-size: 24px; text-align: center;'
    elif val == "🍒":
        return 'background-color: #000000; font-size: 24px; text-align: center;'
    return 'background-color: #111111; color: #444444; font-size: 24px; text-align: center;'

st.write("### Maze")
styled_df = df.style.map(style_game)
st.dataframe(styled_df, width='stretch', hide_index=True)
