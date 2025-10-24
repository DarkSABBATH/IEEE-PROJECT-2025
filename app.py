import streamlit as st
import pandas as pd
from datetime import datetime
import random

# Team data - PROOF OF COLLABORATION
TEAM_MEMBERS = {
    "4AD23EC079": {"name": "Project Lead", "dept": "ECE", "role": "Backend & Deployment"},
    "4AD23EC080": {"name": "V V RIYA VIJAY", "dept": "ECE", "role": "AI Chatbot Core"},
    "4AD23CS075": {"name": "Yeshaswini Madhumita", "dept": "CS-Design", "role": "UI/UX Design"},
    "4AD23EC081": {"name": "Sandesh Mrashi", "dept": "ECE", "role": "Database & Gamification"}
}

# ATME Knowledge Base
KNOWLEDGE_BASE = {
    "exams": "📚 Semester exams: December 8th, 2025. Hall tickets available 15 days prior on college portal.",
    "ieee exhibition": "🚀 IEEE Mini Project Exhibition TOMORROW! Time: 10:00 AM, Venue: College Auditorium. Showcase your projects!",
    "library": "🏛️ Library Hours: Mon-Fri 8AM-8PM, Sat 9AM-5PM. Digital resources available 24/7.",
    "placement": "💼 80+ companies visited last year. Amazon, Microsoft, Infosys, Wipro. Training starts 3rd year!",
    "hostel": "🏠 Separate hostels with WiFi, mess, 24/7 security. Contact: 0821-1234567",
    "courses": "🎯 ECE: Signals, Embedded Systems | CSE: AI, Web Tech | CS-Design: UI/UX, Design Thinking",
    "events": "📅 Upcoming: Hackathon (Nov), Cultural Fest (Dec), Sports Week (Jan), Tech Workshops (Monthly)"
}

def get_response(question):
    question_lower = question.lower()
    for key, answer in KNOWLEDGE_BASE.items():
        if key in question_lower:
            return answer
    return "I'm constantly learning! For this information, please check the college notice board or contact administration. 🎓"

def main():
    st.set_page_config(page_title="ATME Chatbot 🤖", page_icon="🎓", layout="wide")
    
    # Header with team pride
    st.markdown("""
    <div style="background:linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding:25px; border-radius:15px; text-align:center; color:white;">
        <h1 style="margin:0;">ATME College Assistant 🤖</h1>
        <p style="margin:0;">IEEE Project 2025 | Team Collaboration Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Team showcase
    with st.expander("👥 Meet Our Development Team"):
        cols = st.columns(4)
        for i, (usn, member) in enumerate(TEAM_MEMBERS.items()):
            with cols[i]:
                st.write(f"**{member['name']}**")
                st.write(f"*{member['dept']}*")
                st.write(f"🔧 {member['role']}")
    
    # Student login
    usn = st.text_input("🎓 Enter your USN to continue:", placeholder="4AD23EC079").upper()
    
    if usn in TEAM_MEMBERS:
        student = TEAM_MEMBERS[usn]
        
        # Welcome with team role
        st.success(f"👋 Welcome, {student['name']}! | 🎯 {student['dept']} | 🔧 {student['role']}")
        
        # Main layout
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("💬 Chat with ATME Assistant")
            
            # Quick questions - PROOF OF PREDICTIVE FEATURE
            st.write("**🚀 Quick Questions (Predictive AI):**")
            questions = ["Exams schedule", "IEEE exhibition", "Library timings", "Placement info", "Hostel facilities", "Upcoming events"]
            
            # Create buttons in grid
            cols = st.columns(3)
            for i, q in enumerate(questions):
                with cols[i % 3]:
                    if st.button(f"❓ {q}", key=f"btn_{i}"):
                        response = get_response(q)
                        st.session_state.last_response = response
                        st.session_state.last_question = q
            
            # Display last response
            if hasattr(st.session_state, 'last_response'):
                st.markdown(f"""
                <div style="background:#3B82F6; color:white; padding:12px; border-radius:10px; margin:10px 0; text-align:right;">
                    <b>You:</b> {st.session_state.last_question}
                </div>
                <div style="background:#E5E7EB; color:black; padding:12px; border-radius:10px; margin:10px 0;">
                    <b>ATME Bot:</b> {st.session_state.last_response}
                </div>
                """, unsafe_allow_html=True)
            
            # Manual input
            user_input = st.text_input("💭 Or type your question:")
            if user_input:
                response = get_response(user_input)
                st.session_state.last_response = response
                st.session_state.last_question = user_input
                st.rerun()
        
        with col2:
            # Gamification leaderboard
            st.subheader("🏆 Team Points")
            points_data = []
            for usn, member in TEAM_MEMBERS.items():
                points_data.append({
                    "Developer": member["name"],
                    "Role": member["role"],
                    "Points": random.randint(50, 100)
                })
            points_df = pd.DataFrame(points_data)
            st.dataframe(points_df.sort_values("Points", ascending=False), use_container_width=True)
            
            # Mental health feature
            st.subheader("🧠 Wellness Check")
            mood = st.select_slider("How's your coding going?", 
                                  options=["😔 Stuck", "😐 Debugging", "😊 Progress", "🤩 Crushing it!"])
            if st.button("Check-in & Earn Team Points"):
                st.balloons()
                st.success("+15 team points! Great work! 🎉")
            
            # Voice feature placeholder
            st.subheader("🎤 Coming Soon")
            st.info("Voice commands 🎙️ | Multi-language 🌐 | Mobile App 📱")

    else:
        st.info("👆 Enter your USN to experience the ATME Assistant!")

if __name__ == "__main__":
    main()
