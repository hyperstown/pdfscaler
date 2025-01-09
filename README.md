# Simple PDF scaler based on pypdf

A simple program that let's you resize your PDFs to desired format (eg. A4).

### Installation:
- Put binary file into user apps directory:
    - For Linux: `~/.local/bin/`
    - For Windows `%USERPROFILE%\AppData\Local\Programs\`
    - For MacOS `~/bin/`
- Done

*Binary for Linux x86-64 can be found in [Releases](https://github.com/hyperstown/pdfscaler/releases), 
for Windows and MacOS you have to [build it yourself](#building).*

### Usage:

```bash
$ pdfscaler [-h] [-o OUTPUT] {A0,A1,A2,A3,A4,A5,A6,A7,A8,C4} input_pdf
```
 
Example:
```bash
$ pdfscaler A4 a5_document.pdf
```

### Building:

-  Make sure that Python is installed:

    ```bash
    $ python -V
    ```

- Clone repository:

    ```bash
    $ git clone https://github.com/hyperstown/pdfscaler.git`
    ```

- Build (Linux)

    ```bash
    $ bash build.sh
    ```

If you're using Windows or MacOS you have to follow steps from the script manually.
