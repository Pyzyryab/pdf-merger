import PyPDF2
import sys


operation = sys.argv[1]

merger_inputs = sys.argv[2:]
def pdf_combiner(pdf_list):
	'''Given PDF's files merge them into only one'''
	pdf_name = str(input('How will your merged PDF will be named?\n') + '.pdf')
	#Creating a merger object
	merger = PyPDF2.PdfFileMerger()

	for pdf in pdf_list:
		print('Appeding your files. Wait...')
		merger.append(pdf)

	merger.write(pdf_name)


def watermarker(pdf_list):

	pdf_name = str(input('How will your watermarked PDF will be named?\n') + '.pdf')

	original = PyPDF2.PdfFileReader(open(pdf_list[0], 'rb'))
	watermark = PyPDF2.PdfFileReader(open(pdf_list[1], 'rb'))
	output = PyPDF2.PdfFileWriter()

	for i in range(original.getNumPages()):
		page = original.getPage(i)
		page.mergePage(watermark.getPage(0))
		output.addPage(page)

		with open(pdf_name, 'wb') as file:
			output.write(file)


#Choose

if operation == "-m":

	pdf_combiner(merger_inputs)

elif operation == "-w":

	watermarker(merger_inputs)

else:

	print('Por favor, usa -m si quieres unir PDF\'s o -w si quieres poner a un PDF una marca de agua.')