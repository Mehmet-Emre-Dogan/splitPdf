<div align="center">
<img src="https://github.com/Mehmet-Emre-Dogan/splitPdf/blob/main/img.png"> </img>
<br>
</div>

# splitPdf
Split PDF files

# Usage

## .exe File 
- Copy the exe to where PDF is (or copy the PDF where exe is)
- Launch cmd in that directory
- Type `splitPdf` `input_file` `start_page` `end_page` `output_file`

## .py File
- Install the libraries in the `requirements.txt`
- Copy the py file to where PDF is (or copy the PDF where py is)
- Launch cmd in that directory
- Type `python` `splitPdf.py` `input_file` `start_page` `end_page` `output_file`

## General Notes
- Note 1: `start_page` `end_page` are inclusive, i.e., `1` `3` makes use of pages 1, 2, and 3.
- Note 2: `output_file` is optional. If not specified, an automatic name (Splitted__YYYY-MM-DD_HH.mm.ss.pdf) will be genereated

# Images
<div align="center">
<img src="https://github.com/Mehmet-Emre-Dogan/splitPdf/blob/main/images/window.png"> </img>
<br><br>
<img src="https://github.com/Mehmet-Emre-Dogan/splitPdf/blob/main/images/cmd.png"> </img>
</div>

# Acknowledgements & License
## pypdf2
Copyright (c) 2006-2008, Mathieu Fenniak
Some contributions copyright (c) 2007, Ashish Kulkarni <kulkarni.ashish@gmail.com>
Some contributions copyright (c) 2014, Steve Witham <switham_github@mac-guyver.com>

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

* Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
* The name of the author may not be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
