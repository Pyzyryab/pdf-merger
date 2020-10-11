import PyPDF2
import sys
import argparse


def take_command():

	parser = argparse.ArgumentParser(description='''This is a PDF toolkit suite. 
		Remember to write the relative/absolute path in everyone pdf file you insert or work directly 
		in the same folder of the main script.''')
	
	parser.add_argument('-m', '--merge', dest='merge', nargs='+', help='Merge the desired PDF files into only one.')
	parser.add_argument('-w', '--watermarker', dest='watermarker', nargs= '+', help='Put a watermark into your PDF')
	parser.add_argument('-s', '-splitter', dest='splitter', help='Split PDF pages and save it as a new file')

	options = parser.parse_args()
	
	return options
	

def pdf_combiner(pdf_list):
	
	pdf_name = str(input('How will your merged PDF will be named?\n') + '.pdf')
	
	merger = PyPDF2.PdfFileMerger()
	print('Appeding your files. Wait...')

	for pdf in pdf_list:
		
		merger.append(pdf)

	merger.write(pdf_name)


def pdf_splitter(pdf_list):

	original = PyPDF2.PdfFileReader(open(pdf_list[0], 'rb'))
	original_pdf_name = str(original.getDocumentInfo().title)

	for page in range(original.getNumPages()):
		
		output = PyPDF2.PdfFileWriter()

		selected_page = original.getPage(page)

		output.addPage(selected_page)

		new_splitted_page_name = original_pdf_name + '_p' + str(page + 1) + '.pdf'

		with open(new_splitted_page_name, 'wb') as file:
			
			output.write(file)

		print(f'File {new_splitted_page_name} has been created succesfully.')

	print('Congratulatios! Your files has been saved in your default path')



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

	elif options.splitter:

		pdf_splitter(merger_inputs)

	else:

		print('If you desire, use -h or --help to see how to use the program! :)')
