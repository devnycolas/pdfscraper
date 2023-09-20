import PyPDF2
import pandas as pd
import re

# Abra o arquivo PDF
# pdf_file = open('embaixadas-contatos-arrumados.pdf', 'rb')
pdf_file = open('embaixadas-contatos.pdf', 'rb')

# Crie um objeto PdfReader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Inicialize listas para armazenar as informações
embassies = []
tels = []
emails = []

# Percorra as páginas do PDF
for page in pdf_reader.pages:
    text = page.extract_text()

    # Use expressões regulares para encontrar as informações desejadas
    matches = re.findall(r'Embaixada (.*?)\nTel: ([^\n]*)\n(?:E-mail: ([^\n]*)\n)?', text)

    for match in matches:
        embassy, tel, email = match
        embassies.append("Embaixada" + embassy)
        tels.append(tel)
        emails.append(email)

# Crie um DataFrame do pandas
data = {'Embaixada': embassies, 'Telefone': tels, 'E-mail': emails}
df = pd.DataFrame(data)

# Salve o DataFrame em um arquivo Excel
df.to_excel('embaixadas-contatos.xlsx', index=False)

# Feche o arquivo PDF
pdf_file.close()
