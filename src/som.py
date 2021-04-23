# some python file
import textract


text = textract.process("scrum.pdf")
print(text)