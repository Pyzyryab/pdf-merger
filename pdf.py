import PyPDF2
import sys
import optparse

	

def take_command():

	parser = optparse.OptionParser()
	parser.add_option('-m', '--merge', dest='merge', help='Merge the desired PDF files into only one.')
	parser.add_option('-w', '--watermark', dest='watermark', help='Put a watermark into your PDF')
	
	options, arguments = parser.parse_args()

	return options
	

merger_inputs = sys.argv[2:]
def pdf_combiner(pdf_list, command):
	'''Given PDF's files merge them into only one'''
	pdf_name = str(input('How will your merged PDF will be named?\n') + '.pdf')
	
	#Creating a merger object
	merger = PyPDF2.PdfFileMerger()

	for pdf in pdf_list:
		print('Appeding your files. Wait...')
		merger.append(pdf)

	merger.write(pdf_name)


def watermarker(pdf_list, command):

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

options = take_command()
pdf_combiner(merger_inputs, options.merge)
watermarker(merger_inputs, options.merge)