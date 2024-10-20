# Makefile for LaTeX + BibTeX builds

# Variables
TEXFILE = main               # Main .tex file (without extension)
LATEX = pdflatex             # LaTeX engine
BIBTEX = bibtex              # BibTeX engine
PDFVIEWER = evince           # PDF viewer (optional, can be changed)
FLAGS = -interaction=nonstopmode -halt-on-error  # Flags for pdflatex

# Default target: build the PDF
all: $(TEXFILE).pdf

# Rule for compiling the LaTeX document to PDF
$(TEXFILE).pdf:
	$(LATEX) $(FLAGS) $(TEXFILE).tex     # First pdflatex pass
	$(BIBTEX) $(TEXFILE)                 # Run BibTeX for citations
	$(LATEX) $(FLAGS) $(TEXFILE).tex     # Second pdflatex pass (to resolve references)
	$(LATEX) $(FLAGS) $(TEXFILE).tex     # Third pdflatex pass (to finalize document)

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.bbl *.blg *.toc *.out *.lof *.lot *.fls *.fdb_latexmk

# Clean all generated files, including the PDF
cleanall: clean
	rm -f $(TEXFILE).pdf

# View the PDF (optional)
view: $(TEXFILE).pdf
	$(PDFVIEWER) $(TEXFILE).pdf &

# Phony targets (not actual files)
.PHONY: all clean cleanall view


