#!/usr/bin/env python3
import os
import PyPDF2
from pathlib import Path

def extract_pdf_text(pdf_path, output_path):
    """Extract text from PDF and save to txt file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
            
        with open(output_path, 'w', encoding='utf-8') as out_file:
            out_file.write(text)
        
        print(f"Extracted: {pdf_path.name} -> {output_path.name}")
        
    except Exception as e:
        print(f"Error processing {pdf_path.name}: {str(e)}")

def main():
    # Get all PDFs in current directory
    pdf_files = list(Path('.').glob('*.pdf'))
    
    print(f"Found {len(pdf_files)} PDF files")
    
    for pdf_path in pdf_files:
        # Create output filename by replacing .pdf with .txt
        output_path = pdf_path.with_suffix('.txt')
        extract_pdf_text(pdf_path, output_path)

if __name__ == "__main__":
    main()