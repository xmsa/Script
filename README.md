# Script 

## text_file_translator
### install pakage
``` pip install translators==5.7.0 ```
### run script
``` python text_file_translator.py file_name [new_file_name] ```

## goedel_number
Goedel number calculator
### run script
#### encoding <x,y>:z
  ``` python goedel_number.py x y ```
#### decoding z:<x,y>
  ```python goedel_number.py z ```

## file downloader
download file with textfile and url
### run script
#### download file with url
  ``` python download_file_with_textfile.py url ```
#### decdownload file with txtfile 
  ``` python download_file_with_textfile.py file_name.txt ```
#### decdownload file with txtfile and compress all file download in zip file
  ``` python download_file_with_textfile.py -s file_name.txt ```

## youtube video downloader
download youtube video with textfile and url
### run script
#### download file with url
  ``` python youtube_downloader.py url ```
#### decdownload file with txtfile 
  ``` python youtube_downloader.py file_name.txt ```
## Network manager 
Network manager
#### change DNS
 ``` python network_manage.py --dns ```
#### change Mode
 ``` python network_manage.py --mode ```
#### change Port
 ``` python network_manage.py --port ```
#### Run V2ray-ng  
  [Downlod v2ray core](https://github.com/v2fly/v2ray-core/) and extract to $HOME/.local/etc/

  run with directory path config (Defult:"$HOME/Config_v2ray")

 ``` python managenetwork.py --vpn [--config_dir dir_path ]```

  run with config file path (Defult:$HOME/Config_v2ray/config.json)

 ``` python manage\ network.py --vpn [--config file_path ]```

## Rename file on directory
remove multispace and befor or after . in file name
### run script
``` python rename_file.py```
#### Run script with multi directory
``` python rename_file.py dir1 [dir2 ,...]```

## Subtitle LTR to RTL
fixed RTL Problem on subtitle

### run script
#### with Directory
  ``` python Subtitle_ltr_to_rtl.py <Directory>```
#### with SRT file 
  ``` python Subtitle_ltr_to_rtl.py <SRT file>```

## 🧾 Thesis File Merger for Similarity Checking

This script is designed to **preprocess and merge multiple LaTeX files** of an academic thesis into a single, clean text file — ideal for uploading to similarity detection platforms such as **Hamanandjoo** (همانندجو), which often require a flattened document for accurate analysis.

🔗 You can find this script inside the thesis template directory:
[**Thesis Isfahan template**](https://github.com/xmsa/TexTemplate/tree/main/Thesis%20Isfahan%20template)

---

### ✨ Features:

* Recursively expands LaTeX `\input{}` and `\include{}` directives.
* Ignores content after `\appendix` to limit analysis to main body chapters.
* Removes LaTeX comments (`% ...`) while preserving escaped symbols (e.g., `\%`).
* Outputs a clean `.txt` file ready for similarity/plagiarism check tools.

---


### ⚠️ Important Notes:

* 📂 **Backup First:** Make sure to **create a backup of your thesis files** before running the script. It doesn’t modify existing files, but it's always good practice to back up before preprocessing.
* 📄 **Appendices are excluded** from the output by design, as they are often not required for similarity checks.

---

### ▶️ Example Usage

```bash
cd "Thesis Isfahan template"
python thesis_builder.py Thesis.tex -o cleaned_output.txt
```

> Make sure Python is installed and your working directory includes the full thesis project.


