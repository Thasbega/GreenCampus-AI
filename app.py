import streamlit as st

st.set_page_config(
    page_title="GreenCampus AI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 GreenCampus AI")
st.subheader("Smart Sustainability Assistant for Colleges")

st.markdown("---")

question = st.text_input(
    "Ask a Sustainability Question"
)

if st.button("Get Recommendation"):

    q = question.lower()

    if "electricity" in q or "energy" in q:
        st.success("⚡ Energy Saving Recommendations")

        st.write("✅ Replace traditional bulbs with LED lights")
        st.write("✅ Turn off unused devices")
        st.write("✅ Install motion sensor lighting")
        st.write("✅ Conduct energy awareness programs")

    elif "water" in q:
        st.success("💧 Water Conservation Recommendations")

        st.write("✅ Install smart water meters")
        st.write("✅ Fix leakages immediately")
        st.write("✅ Monitor daily water consumption")
        st.write("✅ Promote water conservation campaigns")

    elif "waste" in q:
        st.success("♻ Waste Management Recommendations")

        st.write("✅ Segregate waste properly")
        st.write("✅ Increase recycling bins")
        st.write("✅ Conduct waste awareness programs")
        st.write("✅ Encourage reusable products")

    elif "transport" in q or "transportation" in q:
        st.success("🚲 Sustainable Transportation Recommendations")

        st.write("✅ Promote cycling")
        st.write("✅ Encourage carpooling")
        st.write("✅ Use electric vehicles")
        st.write("✅ Reduce private vehicle usage")

    else:
        st.success("🌱 Sustainability Recommendations")

        st.write("✅ Save electricity whenever possible")
        st.write("✅ Reduce water wastage")
        st.write("✅ Practice proper waste management")
        st.write("✅ Follow sustainable campus initiatives")

st.markdown("---")

st.subheader("📊 Campus Sustainability Score")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("⚡ Energy Score", "85%")

with col2:
    st.metric("💧 Water Score", "78%")

with col3:
    st.metric("♻ Waste Score", "82%")

st.progress(82)

st.success("Overall Sustainability Score: 82%")

st.markdown("---")

st.write("🌍 Building a Greener and Smarter Campus with AI")