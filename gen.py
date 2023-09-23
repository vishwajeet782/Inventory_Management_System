import streamlit_authenticator as stauth
hashed_passwords = stauth.Hasher(['vishalpatil']).generate()
print(hashed_passwords)