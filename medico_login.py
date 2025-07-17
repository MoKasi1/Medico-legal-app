import streamlit as st

--- Dummy User Database (Replace with real DB later) ---

USERS = { "attorney@example.com": {"name": "Ms. Advocate", "role": "Attorney", "password": "law123"}, "secretary@example.com": {"name": "Secretary Jane", "role": "Secretary", "password": "sec123"}, "head@example.com": {"name": "Mr. Office Head", "role": "Office Head", "password": "head123"}, "intermediary@example.com": {"name": "Intermediary Lungi", "role": "Intermediary", "password": "med123"}, "expert@example.com": {"name": "Dr. Expert", "role": "Expert", "password": "doc123"}, }

--- App Config ---

st.set_page_config(page_title="Medico-Legal Login", page_icon="⚖️", layout="centered") st.title("⚖️ Medico-Legal Negligence Platform") st.markdown("Secure login for all stakeholders involved in medical negligence matters.")

--- Login Form ---

st.subheader("🔐 User Login") email = st.text_input("Email") password = st.text_input("Password", type="password")

if st.button("Login"): user = USERS.get(email) if user and user["password"] == password: st.success(f"Welcome, {user['name']}! Role: {user['role']}") st.session_state.logged_in = True st.session_state.user_info = user else: st.error("Invalid login credentials. Please try again.")

--- Post-login Role-based Redirect (for demo) ---

if st.session_state.get("logged_in"): role = st.session_state.user_info["role"] st.markdown("---") st.subheader(f"📂 {role} Dashboard Preview") if role == "Attorney": st.info("You can view your assigned cases, add notes, and schedule expert consultations.") elif role == "Secretary": st.info("You can upload documents, track case deadlines, and assist attorneys.") elif role == "Office Head": st.info("You can monitor all active cases, assign staff, and generate reports.") elif role == "Intermediary": st.info("You can schedule expert appointments and manage medical records.") elif role == "Expert": st.info("You can submit expert reports and view your case schedule.")

--- Footer ---

st.markdown("---") st.caption("State Medico-Legal Negligence System | Role-based Access Demo")

