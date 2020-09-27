import PyPDF2
import sys
import argparse


def take_command():

	parser = argparse.ArgumentParser(description='This is a PDF toolkit suite')
	
	parser.add_argument('-m', '--merge', dest='merge', nargs='+', help='Merge the desired PDF files into only one.')
	parser.add_argument('-w', '--watermarker', dest='watermarker', nargs= '+', help='Put a watermark into your PDF')
	
	options = parser.parse_args()
	
	return options
	

def pdf_combiner(pdf_list):
	'''Given PDF's files merge them into only one'''
	pdf_name = str(input('How will your merged PDF will be named?\n') + '.pdf')
	
	#Creating a merger object
	merger = PyPDF2.PdfFileMerger()
	print('Appeding your files. Wait...')

	for pdf in pdf_list:
		
		
		merger.append(pdf)

	merger.write(pdf_name)


def pdf_watermarker(pdf_list):

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


if __name__ == '__main__':

	options = take_command()

	merger_inputs = sys.argv[2:]

	if options.merge:
		
		pdf_combiner(merger_inputs)
		print(merger_inputs)

	elif options.watermarker:

		pdf_watermarker(merger_inputs)

	else:

		print('If you desire, use -h or --help to see how to use')