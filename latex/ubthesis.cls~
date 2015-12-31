%%
%% This is file `ubthesis.cls',
%% generated with the docstrip utility.
%%
%% The original source files were:
%%
%% ubthesis.dtx  (with options: `ubthesis')
%% 
%% This is a generated file.
%% 
%% Copyright (C) 2007 by Justin Boffemmyer <jsb23@buffalo.edu>
%% 
%% This file may be distributed and/or modified under the conditions of
%% the LaTeX Project Public License, either version 1.2 of this license
%% or (at your option) any later version.  The latest version of this
%% license is in:
%% 
%%    http://www.latex-project.org/lppl.txt
%% 
%% and version 1.2 or later is part of all distributions of LaTeX version
%% 1999/12/01 or later.
%% 
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ubthesis}[2007/04/27 v1.0 UB Thesis Class]

\ProcessOptions
\LoadClassWithOptions{book}

\RequirePackage[letterpaper,margin=1.25in]{geometry}
\RequirePackage[letterpaper,margin=1.25in]{geometry}
\RequirePackage{fancyhdr}


\addtolength{\headheight}{\baselineskip}
\pagestyle{fancy}
\renewcommand{\sectionmark}[1]{\markright{#1}}
\renewcommand{\chaptermark}[1]{\markright{#1}}
\fancyhf{}

\lhead{\large\emph{\UBT@author}}
\chead{}
\rhead{\large\rightmark}
\lfoot{}
\cfoot{\thepage}
\rfoot{}


\pagestyle{fancy}


\newcommand*{\UBT@author}{}
\newcommand*{\UBT@title}{}
\newcommand*{\UBT@conferral}{}
\newcommand*{\UBT@degree}{}
\newcommand*{\UBT@degreetitle}{}
\newcommand*{\UBT@degrees}{}
\newcommand*{\UBT@dept}{}
\newcommand*{\UBT@cdp}{}
\newcommand*{\UBT@lot}{}
\newcommand*{\UBT@lof}{}
\newcommand*{\UBT@ma}{}
\newcommand*{\UBT@ms}{}
\newcommand*{\UBT@mse}{}
\newcommand*{\UBT@mfa}{}
\newcommand*{\UBT@mmus}{}
\newcommand*{\UBT@murbp}{}
\newcommand*{\UBT@march}{}
\newcommand*{\UBT@phd}{}
\newcommand*{\UBT@ed}{}
\newcommand*{\UBT@nsd}{}
\newcommand*{\UBT@thesis}{}
\newcommand*{\UBT@bibname}{}

\newcommand*{\conferral}{}
\newcommand*{\dept}{}
\newcommand*{\degree}{}
\newcommand*{\makecopyright}{}
\newcommand*{\references}{}


\newenvironment{ubfrontmatter}{}{}
\newenvironment{acknowledgements}{}{}
\newenvironment{abstract}{}{}
\newenvironment{ubbackmatter}{}{}


\let\UBT@cdp\cleardoublepage
\let\UBT@lot\listoftables
\let\UBT@lof\listoffigures


\renewcommand{\UBT@ma}{1}
\renewcommand{\UBT@ms}{2}
\renewcommand{\UBT@mse}{3}
\renewcommand{\UBT@mfa}{4}
\renewcommand{\UBT@mmus}{5}
\renewcommand{\UBT@murbp}{6}
\renewcommand{\UBT@march}{7}
\renewcommand{\UBT@phd}{8}
\renewcommand{\UBT@ed}{9}
\renewcommand{\UBT@nsd}{10}


\renewcommand{\author}[1]{\renewcommand{\UBT@author}{#1}}


\renewcommand{\title}[1]{\renewcommand{\UBT@title}{#1}}


\renewcommand{\conferral}[1]{\renewcommand{\UBT@conferral}{#1}}


\renewcommand{\dept}[1]
{
\renewcommand{\UBT@dept}{Department of \MakeUppercase#1}
}


\renewcommand{\degree}[1]{
\renewcommand{\UBT@degree}{
\ifcase\csname UBT@#1\endcsname\or
Master of Arts\or
Master of Science\or
Master of Engineering\or
Master of Fine Arts\or
Master of Music\or
Master of Urban Planning\or
Master of Architecture\or
Doctor of Philosophy\or
Doctor of Education\or
Doctor of Nursing Science
\fi
}
\renewcommand{\UBT@thesis}{%
\ifcase\csname UBT@#1\endcsname\or
thesis\or
thesis\or
thesis\or
thesis\or
thesis\or
thesis\or
thesis\or
dissertation\or
dissertation\or
dissertation
\fi
}
}


\renewcommand{\maketitle}
{
\begin{center}
\par \LARGE \UBT@title
\end{center}

\vspace{\stretch{1}}

\begin{center}
\par by
\bigskip
\par \Large \UBT@author
\smallskip
\par \large \UBT@conferral
\end{center}

\vspace{\stretch{1}}

\begin{center}
\par A~\UBT@thesis{} submitted to the
\par Faculty of the Graduate School of the
\par State University of New York at Buffalo
\par in partial fulfillment of the requirements for the degree of
\bigskip
\par \UBT@degree
\bigskip
\par \UBT@dept
\end{center}
\thispagestyle{empty}
}


\renewcommand{\makecopyright}{
\vspace*{\fill}
\begin{center}
\par Copyright by
\par \UBT@author
\par \number\year
\end{center}
\cleardoublepage
}


\renewcommand{\cleardoublepage}{
\clearpage
\thispagestyle{empty}
\UBT@cdp
}


\renewcommand{\listoftables}{
\UBT@lot
\addcontentsline{toc}{chapter}{List of Tables}
}


\renewcommand{\listoffigures}{
\UBT@lof
\addcontentsline{toc}{chapter}{List of Figures}
}


\renewcommand{\references}[2][References]
{
\renewcommand{\UBT@bibname}{#1}
\addcontentsline{toc}{chapter}{\UBT@bibname}
\bibliography{#2}
\renewcommand{\bibname}{\UBT@bibname}
}


\renewenvironment{thebibliography}[1]
{
\chapter*{\UBT@bibname}%
\list{\@biblabel{\@arabic\c@enumiv}}%
{
\settowidth\labelwidth{\@biblabel{#1}}%
\leftmargin\labelwidth
\advance\leftmargin\labelsep
\@openbib@code
\usecounter{enumiv}%
\let\p@enumiv\@empty
\renewcommand\theenumiv{\@arabic\c@enumiv}}%
\sloppy
\clubpenalty4000
\@clubpenalty \clubpenalty
\widowpenalty4000%
\sfcode`\.\@m
}
{
\def\@noitemerr{\@latex@warning{Empty `thebibliography' environment}}%
\endlist
}


\renewenvironment{titlepage}
{
}
{
\thispagestyle{empty}
\clearpage
}


\renewenvironment{ubfrontmatter}
{
\pagenumbering{roman}
\pagestyle{plain}
\setcounter{page}{2}
}
{
\pagestyle{fancy}
\cleardoublepage
\pagenumbering{arabic}
}


\renewenvironment{ubbackmatter}
{
\cleardoublepage
\thispagestyle{plain}
\pagestyle{plain}
}
{
\thispagestyle{plain}
\pagestyle{plain}
}


\renewenvironment{acknowledgements}
{
\chapter*{Acknowledgements}
\markboth
{\MakeUppercase{Acknowledgements}}
{\MakeUppercase{Acknowledgements}}
\addcontentsline{toc}{chapter}{Acknowledgements}
}
{
\cleardoublepage
}


\renewenvironment{abstract}
{
\chapter*{Abstract}
\markboth
{\MakeUppercase{Abstract}}
{\MakeUppercase{Abstract}}
\addcontentsline{toc}{chapter}{Abstract}
}
{
\cleardoublepage
}

\endinput
%%
%% End of file `ubthesis.cls'.
