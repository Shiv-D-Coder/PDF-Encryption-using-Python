import PyPDF2 as p

# READING FILE
input_file = input("Enter name of file you want to encrypt: ")
input_stream = p.PdfReader(input_file + ".pdf")

# MAKING NEW FILE
name = input("Enter name of encrypted file: ")
output = p.PdfWriter()

# ENCRYPTION OF FILE
passw = input("Enter password for .pdf file: ")
for idx in range(len(input_stream.pages)):
    output.add_page(input_stream.pages[idx])

output.encrypt(passw, use_128bit=True)

with open(name + ".pdf", "wb") as output_stream:
    output.write(output_stream)