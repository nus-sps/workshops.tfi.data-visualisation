#!/bin/bash

#R -e "Sys.setenv(RSTUDIO_PANDOC='/Applications/RStudio.app/Contents/MacOS/pandoc');rmarkdown::render('how
#.Rmd',output_file='how.html')"
echo "-----------------------------------> Knitting site."
R -e "rmarkdown::clean_site()"
R -e "rmarkdown::render_site(encoding = 'UTF-8')"
#R -e "bookdown::bs4_book(theme = bookdown::bs4_book_theme(), repo = NULL,  lib_dir = "libs", pandoc_args = NULL, extra_dependencies = NULL,   split_bib = FALSE)"
