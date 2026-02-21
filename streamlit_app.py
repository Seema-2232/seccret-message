import streamlit as st
from crypto_utils import generate_key, encrypt_message, decrypt_message

st.title("🔐 Secure Message Encryptor")

if "key" not in st.session_state:
    st.session_state.key = generate_key()

option = st.radio("Choose Operation", ["Encrypt", "Decrypt"])

message = st.text_area("Enter Message")

if st.button("Process"):
    if not message:
        st.warning("Please enter text")
    else:
        if option == "Encrypt":
            result = encrypt_message(message, st.session_state.key)
            st.success("Encrypted Message")
            st.code(result)
        else:
            try:
                result = decrypt_message(message, st.session_state.key)
                st.success("Decrypted Message")
                st.code(result)
            except:
                st.error("Invalid encrypted text or key")