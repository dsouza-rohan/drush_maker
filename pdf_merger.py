import sys
from PyPDF2 import PdfFileMerger,PdfFileWriter,PdfFileReader
import subprocess
import os


class pdfMerge():
    """pdfMerge class"""

    def pdf_cat(input_files):
        input_streams = input_files

        merger = PdfFileMerger()
        for pdf in input_streams:
            merger.append(pdf)

        merger.write("merged{}".format(pdf))

    def pdf_compress(input_files):
        input_streams = input_files

        for pdf in input_streams:
            writer = PdfFileWriter()
            reader = PdfFileReader(pdf)
            for i in range(reader.numPages):
                page = reader.getPage(i)
                page.compressContentStreams()
                writer.addPage(page)

            with open('compress{}'.format(pdf), 'wb') as f:
                writer.write(f)

    def gscompress(input_files, power=0):
        """Function to compress PDF via Ghostscript command line interface"""

        input_streams = input_files
        for input_file_path in input_streams:
            output_file_path = "compress{}_{}".format(power,input_file_path)
            quality = {
                0: '/default',
                1: '/prepress',
                2: '/printer',
                3: '/ebook',
                4: '/screen'
            }

            # Basic controls
            # Check if valid path
            if not os.path.isfile(input_file_path):
                print("Error: invalid path for input PDF file")
                sys.exit(1)

            # Check if file is a PDF by extension
            if input_file_path.split('.')[-1].lower() != 'pdf':
                print("Error: input file is not a PDF")
                sys.exit(1)

            print("Compress PDF...")
            initial_size = os.path.getsize(input_file_path)
            subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                             '-dPDFSETTINGS={}'.format(quality[power]),
                             '-dNOPAUSE', '-dQUIET', '-dBATCH',
                             '-sOutputFile={}'.format(output_file_path),
                             input_file_path]
                            )
            final_size = os.path.getsize(output_file_path)
            ratio = 1 - (final_size / initial_size)
            print("Compression by {0:.0%}.".format(ratio))
            print("Final file size is {0:.1f}MB".format(final_size / 1000000))
            print("Done.")


if __name__ == '__main__':
    pdf = pdfMerge

    print(sys.argv[1:])

    # pdf.pdf_cat(sys.argv[1:])
    # pdf.pdf_compress(sys.argv[1:])
    pdf.gscompress(sys.argv[1:],3)
