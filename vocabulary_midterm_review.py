import streamlit as st
import time

# --- Configuration ---
st.set_page_config(page_title="Unit 10 & 11 Review", page_icon="🎓", layout="centered")

# --- 40-Question Quiz Data ---
quiz_data = [
    # SECTION 1: Appearance and Clothing (Mix of Images and Text)
    {"sec": "Section 1: Appearance & Clothing", "image": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?w=500", "q": "1. Look at the woman's hair. How would you describe it?", "opts": ["dark hair", "fair hair", "curly hair", "short hair"], "ans": "fair hair"},
    {"sec": "Section 1: Appearance & Clothing", "image": "https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Ftheblacktux.com%2Fproducts%2Fessential-true-navy-suit-outfit&ved=0CBYQjRxqFwoTCODq56-6z5UDFQAAAAAdAAAAABA3&opi=89978449", "q": "2. What is the man wearing?", "opts": ["A T-shirt and shorts", "A jacket and trainers", "A suit and tie", "A scarf and boots"], "ans": "A suit and tie"},
    {"sec": "Section 1: Appearance & Clothing", "q": "3. It is very cold today; you should wear a woolly _________ around your neck.", "opts": ["cap", "belt", "scarf", "tie"], "ans": "scarf"},
    {"sec": "Section 1: Appearance & Clothing", "q": "4. I can't see the whiteboard clearly. I think I need to start wearing _________.", "opts": ["trainers", "boots", "glasses", "caps"], "ans": "glasses"},
    {"sec": "Section 1: Appearance & Clothing", "image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500", "q": "5. Look at the man's face. What has he got?", "opts": ["A scarf", "A watch", "Glasses", "A beard"], "ans": "A beard"},
    {"sec": "Section 1: Appearance & Clothing", "q": "6. We are going to the beach, so I’m wearing a T-shirt and _________.", "opts": ["a suit", "a tie", "shorts", "boots"], "ans": "shorts"},
    {"sec": "Section 1: Appearance & Clothing", "image": "https://images.unsplash.com/photo-1531123897727-8f129e1688ce?w=500", "q": "7. How would you describe her hair?", "opts": ["Straight hair", "Fair hair", "Curly hair", "Red hair"], "ans": "Curly hair"},
    {"sec": "Section 1: Appearance & Clothing", "q": "8. These _________ are perfect for running in the park.", "opts": ["shoes", "boots", "trainers", "skirts"], "ans": "trainers"},
    {"sec": "Section 1: Appearance & Clothing", "q": "9. My sister is quite _________, so she usually sits in the front row of photos.", "opts": ["tall", "short", "old", "fair"], "ans": "short"},
    {"sec": "Section 1: Appearance & Clothing", "q": "10. The businessman wore a white shirt and a silk _________.", "opts": ["jacket", "tie", "hat", "dress"], "ans": "tie"},

    # SECTION 2: Weather & Descriptive Adjectives (Fill in the blanks)
    {"sec": "Section 2: Weather & Adjectives", "q": "11. The dinner at the Italian restaurant was __________; I loved the pasta!", "opts": ["foggy", "delicious", "expensive", "old"], "ans": "delicious"},
    {"sec": "Section 2: Weather & Adjectives", "image": "https://images.unsplash.com/photo-1485236715568-ddc5ee6ca227?w=500", "q": "12. Be careful driving this morning; it is very __________ and you can't see the road.", "opts": ["sunny", "stormy", "foggy", "relaxed"], "ans": "foggy"},
    {"sec": "Section 2: Weather & Adjectives", "q": "13. We went to the mountains for a __________ holiday; there was white powder everywhere.", "opts": ["snowy", "peaceful", "huge", "sunny"], "ans": "snowy"},
    {"sec": "Section 2: Weather & Adjectives", "q": "14. The hotel was too __________ for us, so we stayed in a cheaper hostel.", "opts": ["old", "relaxed", "expensive", "delicious"], "ans": "expensive"},
    {"sec": "Section 2: Weather & Adjectives", "q": "15. The city center is always busy, but the park is very __________ and quiet.", "opts": ["peaceful", "stormy", "huge", "foggy"], "ans": "peaceful"},
    {"sec": "Section 2: Weather & Adjectives", "q": "16. Look at that __________ cruise ship! It looks like a floating city.", "opts": ["delicious", "relaxed", "huge", "foggy"], "ans": "huge"},
    {"sec": "Section 2: Weather & Adjectives", "q": "17. After a long week of work, I felt very __________ during my weekend at the spa.", "opts": ["stormy", "relaxed", "old", "snowy"], "ans": "relaxed"},
    {"sec": "Section 2: Weather & Adjectives", "q": "18. We stayed inside because the weather was __________ with loud thunder and lightning.", "opts": ["sunny", "stormy", "peaceful", "expensive"], "ans": "stormy"},
    {"sec": "Section 2: Weather & Adjectives", "q": "19. This __________ building was built over three hundred years ago.", "opts": ["huge", "old", "delicious", "snowy"], "ans": "old"},
    {"sec": "Section 2: Weather & Adjectives", "q": "20. It is a beautiful __________ day; let's go for a walk in the garden.", "opts": ["sunny", "foggy", "stormy", "expensive"], "ans": "sunny"},

    # SECTION 3: Places and Purposes (Matching/QCMs)
    {"sec": "Section 3: Places & Purposes", "image": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=500", "q": "21. Why are these people at the gym?", "opts": ["To do exercise", "To get a train", "To see a play", "To have a haircut"], "ans": "To do exercise"},
    {"sec": "Section 3: Places & Purposes", "q": "22. Why do you go to a restaurant?", "opts": ["To give a presentation", "To have lunch", "To buy a present", "To get a flight"], "ans": "To have lunch"},
    {"sec": "Section 3: Places & Purposes", "q": "23. Why do people attend a conference?", "opts": ["To see an exhibition", "To do exercise", "To give a presentation", "To pick kids up"], "ans": "To give a presentation"},
    {"sec": "Section 3: Places & Purposes", "q": "24. Why do you go to a shop?", "opts": ["To buy a present", "To have a haircut", "To see a play", "To get a train"], "ans": "To buy a present"},
    {"sec": "Section 3: Places & Purposes", "q": "25. Why do parents go to a school in the afternoon?", "opts": ["To get a flight", "To pick their kids up", "To see an exhibition", "To have lunch"], "ans": "To pick their kids up"},
    {"sec": "Section 3: Places & Purposes", "q": "26. Why do you visit the barber's?", "opts": ["To see a play", "To do exercise", "To have a haircut", "To give a presentation"], "ans": "To have a haircut"},
    {"sec": "Section 3: Places & Purposes", "q": "27. Why do people go to the theatre?", "opts": ["To get a train", "To see a play", "To buy a present", "To pick kids up"], "ans": "To see a play"},
    {"sec": "Section 3: Places & Purposes", "image": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=500", "q": "28. Why do people go to the airport?", "opts": ["To get a flight", "To see an exhibition", "To have a haircut", "To do exercise"], "ans": "To get a flight"},
    {"sec": "Section 3: Places & Purposes", "image": "https://images.unsplash.com/photo-1572949645841-094f3a9c4c94?w=500", "q": "29. Why are these people at the art gallery?", "opts": ["To get a train", "To see an exhibition", "To give a presentation", "To have lunch"], "ans": "To see an exhibition"},
    {"sec": "Section 3: Places & Purposes", "q": "30. Why do you go to a railway station?", "opts": ["To see a play", "To get a train", "To buy a present", "To pick kids up"], "ans": "To get a train"},

    # SECTION 4: Linking Words (Fill in the blanks)
    {"sec": "Section 4: Linking Words", "q": "31. I wanted to go for a run, __________ it started to rain heavily.", "opts": ["but", "so", "because", "although"], "ans": "but"},
    {"sec": "Section 4: Linking Words", "q": "32. I bought a new jacket __________ my old one was too small.", "opts": ["when", "so", "because", "however"], "ans": "because"},
    {"sec": "Section 4: Linking Words", "q": "33. __________ it was a very expensive restaurant, the food wasn't very good.", "opts": ["Although", "But", "So", "Because"], "ans": "Although"},
    {"sec": "Section 4: Linking Words", "q": "34. It was a very windy day, __________ we decided not to go sailing.", "opts": ["although", "because", "so", "however"], "ans": "so"},
    {"sec": "Section 4: Linking Words", "q": "35. He is very handsome; __________, he is also very shy.", "opts": ["but", "so", "however", "because"], "ans": "however"},
    {"sec": "Section 4: Linking Words", "q": "36. __________ I am on holiday, I like to wake up late and feel relaxed.", "opts": ["But", "When", "So", "However"], "ans": "When"},
    {"sec": "Section 4: Linking Words", "q": "37. She wears glasses __________ she needs them for reading.", "opts": ["because", "but", "although", "so"], "ans": "because"},
    {"sec": "Section 4: Linking Words", "q": "38. The museum was very busy, __________ we managed to see the famous painting.", "opts": ["so", "because", "but", "when"], "ans": "but"},
    {"sec": "Section 4: Linking Words", "q": "39. I am going to the barber's __________ I need a haircut for the interview.", "opts": ["although", "but", "however", "because"], "ans": "because"},
    {"sec": "Section 4: Linking Words", "q": "40. It was snowing, __________ the children went outside to play.", "opts": ["so", "because", "although", "when"], "ans": "so"}
]

# --- State Management ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None

# --- Main App UI ---
st.title("🎓 Unit 10 & 11 Mastery Quiz")
st.write("Test your vocabulary, grammar, and reading skills!")

# Check if the quiz is finished
if st.session_state.current_q >= len(quiz_data):
    st.balloons()
    st.success(f"🎉 Exam Complete! Final Score: **{st.session_state.score} / {len(quiz_data)}**")
    st.progress(1.0)
    
    if st.button("Restart Exam 🔄"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.submitted = False
        st.rerun()
else:
    # Load Current Question Data
    q_data = quiz_data[st.session_state.current_q]
    
    # Display Progress and Current Section
    progress_val = st.session_state.current_q / len(quiz_data)
    st.progress(progress_val, text=f"Question {st.session_state.current_q + 1} of {len(quiz_data)}")
    st.markdown(f"### {q_data['sec']}")
    
    # Render Image if the question has one
    if "image" in q_data:
        st.image(q_data["image"], use_column_width=True)
    
    st.write(f"**{q_data['q']}**")
    
    # Form for submission
    with st.form(key=f"q_form_{st.session_state.current_q}"):
        
        # Adapting the prompt based on the section style
        if "Fill in the blank" in q_data.get('q', '') or "_________" in q_data['q']:
            prompt_text = "Select the word that best fills the blank:"
        else:
            prompt_text = "Choose the correct answer:"
            
        choice = st.radio(prompt_text, q_data["opts"], key="quiz_radio")
        submit_button = st.form_submit_button(label="Submit Answer ✅")

        if submit_button:
            st.session_state.submitted = True
            st.session_state.selected_option = choice

    # Feedback and progression
    if st.session_state.submitted:
        if st.session_state.selected_option == q_data["ans"]:
            st.success("🌟 Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect. The correct answer is: **{q_data['ans']}**")
        
        # Brief pause for students to read the feedback
        time.sleep(0.5)
        
        if st.button("Next Question ➡️", type="primary"):
            st.session_state.current_q += 1
            st.session_state.submitted = False
            st.session_state.selected_option = None
            st.rerun()

# --- Sidebar ---
st.sidebar.header("Scoreboard")
st.sidebar.metric(label="Score", value=f"{st.session_state.score} / {len(quiz_data)}")

# Section overview tracker
st.sidebar.markdown("---")
st.sidebar.markdown("**Exam Sections:**")
st.sidebar.markdown("- 🧑‍🦱 Appearance & Clothing (1-10)")
st.sidebar.markdown("- ☀️ Weather & Adjectives (11-20)")
st.sidebar.markdown("- 🏫 Places & Purposes (21-30)")
st.sidebar.markdown("- 🔗 Linking Words (31-40)")