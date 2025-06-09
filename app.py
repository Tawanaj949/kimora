import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Agent Kimora - Real Estate Concierge",
    page_icon="🏡",
    layout="centered",
)

# --- Header ---
st.title("👩🏾‍💼 Agent Kimora")
st.subheader("Design. Search. Manage.")
st.markdown("**Your Personal Real Estate Concierge for Investors & Buyers**")

# --- About Section ---
st.markdown("### 🔍 Who is Agent Kimora?")
st.write("""
Agent Kimora is your trusted partner in real estate investment and property management. 
She specializes in designing, searching, and managing real estate deals for investors and buyers—charging only a small percentage for premium service.
""")

# --- Services Section ---
st.markdown("### 🛠️ Services Offered")
st.markdown("""
- ✅ Property Search & Acquisition  
- ✅ Real Estate Investment Fund Management  
- ✅ Design-to-Sell / Design-to-Rent Consulting  
- ✅ Hands-Free Property Management  
- ✅ Investor Concierge Support  
""")

# --- Value Proposition ---
st.markdown("### 💼 Why Work With Agent Kimora?")
st.markdown("""
- Strategic property selection with your ROI in mind  
- Creative design solutions to enhance property value  
- Streamlined communication, paperwork, and compliance  
- Trusted oversight while you stay hands-off  
""")

# --- Call to Action ---
st.markdown("### 📅 Schedule a Consultation")
name = st.text_input("Your Name")
email = st.text_input("Your Email")
service_interest = st.selectbox("Interested In", ["Property Search", "Investment Management", "Design Services", "Full Management", "Other"])
message = st.text_area("Tell Agent Kimora what you need...")

if st.button("Submit Request"):
    st.success(f"Thank you {name}! Agent Kimora will contact you shortly at {email}.")

# --- Footer ---
st.markdown("---")
st.markdown("🔗 Powered by **Agent Kimora** | Real Estate Concierge & Investment Management")

