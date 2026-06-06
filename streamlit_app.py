import streamlit as st
import requests

# ====================== PAGE CONFIG & GIRLY STYLE ======================
st.set_page_config(
    page_title="PinkGuard AI",
    page_icon="💖",
    layout="wide"
)

# Custom soft pink & girly CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #ffeef8, #fff0f5);
    }
    .main-header {
        font-size: 42px;
        color: #ff69b4;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
    }
    .stButton>button {
        background: #ff69b4;
        color: white;
        border-radius: 20px;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: #ff1493;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ====================== HEADER ======================
st.markdown('<h1 class="main-header">💖 PinkGuard AI Fraud Detector</h1>', unsafe_allow_html=True)
st.markdown("### *Protecting your transactions with love & smart AI* 🌸")

# ====================== SIDEBAR ======================
with st.sidebar:
    st.header("💕 How to Use")
    st.write("""
    1. Choose a **sample transaction** below (recommended)
    2. Or manually type **Time** and **Amount**
    3. Click the big pink **Predict** button
    4. Get instant result!
    """)
    
    st.divider()
    st.caption("The 28 hidden features (V1–V28) are automatically set by the AI so you don’t have to worry about them 💖")

# ====================== MAIN INPUTS ======================
st.subheader("📌 Enter Transaction Details")

col1, col2 = st.columns(2)

with col1:
    time = st.number_input(
        "⏰ Time (seconds since first transaction)",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        help="Usually between 0 and 170000"
    )

with col2:
    amount = st.number_input(
        "💰 Amount ($)",
        min_value=0.0,
        value=50.0,
        step=10.0,
        format="%.2f"
    )

# ====================== SAMPLE BUTTONS (Automated) ======================
st.subheader("🎀 Load Sample Transactions")

st.write("**Click one of these buttons** – it will automatically fill everything for you:")

sample_col1, sample_col2 = st.columns(2)

with sample_col1:
    if st.button("💖 Everyday Safe Purchase", use_container_width=True):
        # Normal transaction
        st.session_state.features = [0.0] * 28 + [time, amount]
        st.session_state.features[28] = 12000.0   # realistic time
        st.session_state.features[29] = 42.50     # realistic amount
        st.success("✅ Safe everyday purchase loaded! (Low risk)")

with sample_col2:
    if st.button("🚨 High-Risk Test Transaction", use_container_width=True):
        # Suspicious transaction
        st.session_state.features = [0.0] * 28 + [time, amount]
        st.session_state.features[28] = 85000.0   # late time
        st.session_state.features[29] = 1899.99   # very high amount
        st.warning("⚠️ High-risk example loaded!")

# Show current values (optional)
if st.checkbox("Show full 30 features (for advanced users)"):
    st.write(st.session_state.get('features', [0.0]*30))

# ====================== PREDICT BUTTON ======================
if st.button("🔍 CHECK FOR FRAUD", type="primary", use_container_width=True):
    with st.spinner("💖 Analyzing transaction with AI..."):
        try:
            # Prepare the 30 features (hidden ones are already set by samples)
            if 'features' not in st.session_state:
                st.session_state.features = [0.0] * 30
            st.session_state.features[28] = time
            st.session_state.features[29] = amount

            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json={"features": st.session_state.features},
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()
                prob = result.get("fraud_probability", 0)

                st.subheader("✨ Prediction Result")

                if result.get("prediction") == 1:
                    st.error(f"🚨 **FRAUD DETECTED** 💔")
                    st.write(f"**Fraud Probability:** `{prob:.1%}`")
                else:
                    st.success(f"✅ **Safe & Legitimate** 💖")
                    st.write(f"**Fraud Probability:** `{prob:.1%}`")

                st.progress(prob)
            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error(f"💔 Cannot connect to the API. Make sure app.py is running!")

# ====================== FOOTER ======================
st.divider()
st.markdown("Made with 💕 for beautiful & safe shopping | Streamlit + Flask + PinkGuard AI")
