# PrinterTpvBelleza

Instalar a nivel global las dependencia de python necesarias .
sudo -H pip3 install -r requirements.txt

Copiar el servicio de impresora
cp epson.service  /lib/systemd/system

Copiar 71-epson.rules
cp 71-epson.rules /lib/udev/rules.d
sudo  udevadm control --reload-rules && sudo udevadm trigger

Arracar y parar el servicio

systemctl start epson
systemctl stop epson

curl --header "Content-Type: application/json" --request POST -d @ticket.json http://localhost:5000/print_ticket/
curl http://localhost:5000/configure/tres/cuatro
udevadm monitor --kernel --property --subsystem-match=usb

