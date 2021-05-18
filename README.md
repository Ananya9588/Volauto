# VOLAUTO - Let's automate Volatility

![Screenshot_20210518_142507](https://user-images.githubusercontent.com/54741372/118622571-12754080-b7e5-11eb-83d7-ad30410fbf94.png)

# Prerequisite 

```
cd volauto/
chmod +x setup_debian.sh  --- if using debian based system 
or use 
chmod +x setup_arch.sh --  if using arch based system
./setup_debian.sh 
or
./setup_arch.sh
```

# Usage
```
python3 volauto.py -f filename
```


# Description

Volauto is a volatility automation tool it allows you to automate basic enumeration to important file downloads of the forensic file.
All you need to do is just pass the filename and rest will be taken care by the script.
Output will be saved in the output directory for further analysis. 

#### Commands will be executed by the tool
1. Imageinfo of the file 
2. Process Info of the suitable profile
3. Command Line
4. Environment Variable
5. Consoles
6. Master File Table info
7. Filescan 
8. Filescan for Desktop
9. Filescan for Downloads
10. Filescan for Users
11. Chromehistory
12. Firefox History
13. IEhistory
14. File Dump of extentions such as jpg,png,txt,pdf,zip,rar
15. Process dump
16. Notepad
17. Clipboard
18. Hash dump
19. Process Tree

>Open for Suggestion you can ping me on https://www.linkedin.com/in/ananyamishra9588
