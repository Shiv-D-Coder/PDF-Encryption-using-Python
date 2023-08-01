import PyPDF2 as p

# READING FILE
input_file = input("Enter name of file you want to encrypt: ")

# Open the input PDF file using PdfReader
input_stream = p.PdfReader(input_file + ".pdf")

# MAKING NEW FILE
name = input("Enter name of encrypted file: ")

# Create a PdfWriter object to store the output PDF
output = p.PdfWriter()

# ENCRYPTION OF FILE
passw = input("Enter password for .pdf file: ")

# Loop through each page of the input PDF and add it to the output PdfWriter
for idx in range(len(input_stream.pages)):
    output.add_page(input_stream.pages[idx])

# Encrypt the output PDF using the provided password and 128-bit encryption
output.encrypt(passw, use_128bit=True)

# Write the encrypted output PDF to the specified output file
with open(name + ".pdf", "wb") as output_stream:
    output.write(output_stream)
