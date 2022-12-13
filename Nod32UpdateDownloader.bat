@echo off
cd C:\xampp\htdocs\Nod32Update
wget -v -N --timeout=900 -r -l1 --no-parent -A"*.ver,*.nup" -nd http://antivirus.uclv.cu/update/nod32/eset_updv8/
if exist Nod32Update.rar del Nod32Update.rar
rar a Nod32Update.rar *.ver *.nup
