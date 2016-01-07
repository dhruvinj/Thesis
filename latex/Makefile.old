.PHONY all: code doc example

code:
	latex ubthesis.ins

doc:
	latex ubthesis.dtx
	latex ubthesis.dtx
	latex ubthesis.dtx
	makeindex -s gglo.ist -o ubthesis.gls ubthesis.glo
	makeindex -s gind.ist -o ubthesis.ind ubthesis.idx
	latex ubthesis.dtx
	dvipdf ubthesis.dvi
	references.bib

example:
	latex thesis.tex
	latex thesis.tex
	latex thesis.tex
	dvipdf thesis.dvi

.PHONY clean: clean-doc

.PHONY clean-all: clean-doc clean-example clean-code
	rm -f *.pdf

clean-code:
	rm ubthesis.cls
	rm thesis.tex

clean-doc:
	rm -f ubthesis.aux
	rm -f ubthesis.dvi
	rm -f ubthesis.glo
	rm -f ubthesis.gls
	rm -f ubthesis.idx
	rm -f ubthesis.ilg
	rm -f ubthesis.ind
	rm -f ubthesis.log

clean-example:
	rm -f thesis.aux
	rm -f thesis.dvi
	rm -f thesis.lof
	rm -f thesis.log
	rm -f thesis.lot
	rm -f thesis.toc

