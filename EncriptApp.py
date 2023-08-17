import streamlit as st
import PyPDF2 as p

st.set_page_config(
    page_icon=":🔐:",
    page_title="PDF-ENCRIPTER App"
)

def main():
    st.title("PDF Encryption🔒")

    st.write("Drop your PDF below")
    uploaded_file = st.file_uploader("Upload")

    passw = st.sidebar.text_input("Enter the password for the PDF file:")

    if uploaded_file:
        st.success("File uploaded successfully!")

        if passw and st.button("Encrypt"):
            input_stream = p.PdfReader(uploaded_file)

            st.write("Encryption in progress...")

            output = p.PdfWriter()

            for idx in range(len(input_stream.pages)):
                output.add_page(input_stream.pages[idx])

            output.encrypt(passw, use_128bit=True)

            encrypted_filename = "EncryptedFile.pdf"

            with open(encrypted_filename, "wb") as output_stream:
                output.write(output_stream)

            st.success(f"Encryption successful! Encrypted PDF saved as {encrypted_filename}")

            st.download_button(
                label="Download Encrypted PDF",
                data=open(encrypted_filename, "rb").read(),
                file_name=encrypted_filename
            )

if __name__ == "__main__":
    main()
