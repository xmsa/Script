# Mini Project

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